from collections import Counter
from datasets import load_dataset, Dataset, concatenate_datasets

def get_kaggle_env(config):
    def get_train_data():
        # https://huggingface.co/datasets/AI-MO/aimo-validation-amc
        dataset = load_dataset(config.validation_set, split="train[:10]") # replace with `train` to evaluate over the full validation set
        dataset = dataset.map(lambda x: {'answer': str(int(x['answer']) % 1000)})
        df = dataset.to_pandas()
        return df

    class train_env:
        def __init__(self, shuffle=False):
            self.shuffle = shuffle
            self.df = get_train_data()
            self.df["ground_truth"] = self.df["answer"]
            self.df["answer"] = -1
            if self.shuffle:
                self.df = self.df.reset_index().sample(frac=1).reset_index(drop=True)
            self.predict_called = True
            self.counter = 0
            self.len = len(self.df)

        def iter_test(self):
            while self.counter < self.len:
                if self.predict_called:
                    self.predict_called = False
                    yield (self.df.loc[[self.counter]][["id", "problem"]]), (self.df.loc[[self.counter]][["id", "answer"]])
                else:
                    print("You must call `predict()` successfully before you can continue with `iter_test()`")
                    yield None

        def predict(self, answer):
            self.df[self.counter, "answer"] = answer["answer"]
            self.predict_called = True
            self.counter += 1

    env = train_env(shuffle=True)
    iter_test = env.iter_test()

    return env, iter_test

def filter_answers(answers):
    def validate_answer_is_numeric(x, tolerance=0.2):
        try:
            x = round(float(x))
            f = float(x)
            if abs(x - f) > tolerance:
                x = -1
        except Exception:
            x = -1
        return x

    formatted = [validate_answer_is_numeric(a) for a in answers]
    filtered = [a % 1000 for a in formatted if a >= 0]
    return filtered


def get_majority_vote(answers):
    if not len(answers):
        return 0
    c = Counter(answers)
    value, _ = c.most_common()[0]
    return value

