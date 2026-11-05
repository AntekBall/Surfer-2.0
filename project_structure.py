from pathlib import Path

ROOT = Path(r"C:\Users\antek\surfer2.0")

DIRECTORIES = [
    "configs",
    r"data\receptors",
    r"data\ligands",
    r"data\docking",
    r"data\processed\fingerprints",
    r"data\processed\graphs",
    r"data\processed\datasets",
    "scripts",
    r"src\data",
    r"src\features",
    r"src\models",
    r"src\training",
    r"src\utils",
    r"models\checkpoints",
    r"results\figures",
    r"results\metrics",
    "logs",
    "tests",
]

FILES = [
    # Project configuration
    "README.md",
    "requirements.txt",
    ".gitignore",
    r"configs\docking.yaml",
    r"configs\model.yaml",
    r"configs\training.yaml",

    # Pipeline execution scripts
    r"scripts\01_extract_vina.py",
    r"scripts\02_export_poses.py",
    r"scripts\03_build_fingerprints.py",
    r"scripts\04_build_graphs.py",
    r"scripts\05_build_dataset.py",
    r"scripts\06_train.py",
    r"scripts\07_evaluate.py",

    # Data extraction and loading
    r"src\__init__.py",
    r"src\data\__init__.py",
    r"src\data\vina_parser.py",
    r"src\data\structure_loader.py",
    r"src\data\dataset.py",

    # Feature engineering
    r"src\features\__init__.py",
    r"src\features\morgan.py",
    r"src\features\graph3d.py",
    r"src\features\interactions.py",

    # Neural network architecture
    r"src\models\__init__.py",
    r"src\models\fingerprint_mlp.py",
    r"src\models\gnn3d.py",
    r"src\models\fusion.py",

    # Model training
    r"src\training\__init__.py",
    r"src\training\trainer.py",
    r"src\training\evaluator.py",

    # Utilities
    r"src\utils\__init__.py",
    r"src\utils\metrics.py",

    # Tests
    r"tests\__init__.py",
    r"tests\test_vina_parser.py",
    r"tests\test_fingerprints.py",
    r"tests\test_graph3d.py",
    r"tests\test_models.py",
]


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    for directory in DIRECTORIES:
        (ROOT / Path(directory.replace("\\", "/"))).mkdir(
            parents=True,
            exist_ok=True
        )

    created = 0

    for filename in FILES:
        path = ROOT / Path(filename.replace("\\", "/"))
        path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with path.open("xb"):
                pass
        except FileExistsError:
            if not path.is_file():
                raise
        else:
            created += 1

    print(f"Created {created} empty files in {ROOT}")
    print("Existing files were left unchanged.")


if __name__ == "__main__":
    main()