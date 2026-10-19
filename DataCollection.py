def load_Dataset():
    import kagglehub
    import os
    import pandas as pd

    try:
        # Kaggle dataset
        url = "adarshsng/lending-club-loan-data-csv"

        # Download dataset
        path = kagglehub.dataset_download(url)

        # Find the CSV file
        csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]

        if not csv_files:
            raise FileNotFoundError("No CSV file found in the downloaded dataset.")

        loan_file_path = os.path.join(path, csv_files[0])
        print("File path = ",loan_file_path)

        # Load dataset
        df = pd.read_csv(loan_file_path)

        print("Dataset loaded successfully!")
        print(f"Shape: {df.shape}")

        return df

    except Exception as e:
        print(f"load_Dataset --> Error: {e}")
        return None