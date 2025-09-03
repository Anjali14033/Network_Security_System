from dataclasses import dataclass #with the help of dataclasses we can create classes that are mainly used to store data(It  acts like a decorator that creates variable for an empty class)

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str