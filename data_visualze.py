import pandas as pd
import matplotlib.pyplot as plt
import warnings
import os

warnings.filterwarnings('ignore')


def data_visualize(df, save_folder="visuals"):

    # Create folder if not exists
    os.makedirs(save_folder, exist_ok=True)

    # 1️⃣ Gender Distribution
    plt.figure(figsize=(5, 5))
    df['gender'].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Gender Distribution")
    plt.ylabel("")
    plt.savefig(f"{save_folder}/gender.png")
    plt.close()

    # 2️⃣ Phone Service
    plt.figure(figsize=(5, 4))
    df['PhoneService'].value_counts().plot(kind="bar")
    plt.title("Phone Service Distribution")
    plt.savefig(f"{save_folder}/phone_service.png")
    plt.close()

    # 3️⃣ Contract
    plt.figure(figsize=(5, 5))
    df['Contract'].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Contract Distribution")
    plt.ylabel("")
    plt.savefig(f"{save_folder}/contract.png")
    plt.close()

    # 4️⃣ Churn
    plt.figure(figsize=(5, 4))
    df['Churn'].value_counts().plot(kind="bar")
    plt.title("Churn Distribution")
    plt.savefig(f"{save_folder}/churn.png")
    plt.close()

    # 5️⃣ Phone vs Internet
    plt.figure(figsize=(6, 4))
    pd.crosstab(df["PhoneService"], df["InternetService"]).plot(kind="bar")
    plt.title("Phone Service vs Internet Service")
    plt.xlabel("Phone Service")
    plt.ylabel("Customer Count")
    plt.savefig(f"{save_folder}/phone_vs_internet.png")
    plt.close()

    # 6️⃣ Gender vs Churn
    plt.figure(figsize=(6, 4))
    pd.crosstab(df["gender"], df["Churn"]).plot(kind="bar")
    plt.title("Gender vs Churn")
    plt.savefig(f"{save_folder}/gender_vs_churn.png")
    plt.close()

    # 7️⃣ Internet vs Churn
    plt.figure(figsize=(6, 4))
    pd.crosstab(df["InternetService"], df["Churn"]).plot(kind="bar")
    plt.title("Internet Service vs Churn")
    plt.savefig(f"{save_folder}/internet_vs_churn.png")
    plt.close()

    # 8️⃣ Contract vs Churn
    plt.figure(figsize=(6, 4))
    pd.crosstab(df["Contract"], df["Churn"]).plot(kind="bar")
    plt.title("Contract vs Churn")
    plt.savefig(f"{save_folder}/contract_vs_churn.png")
    plt.close()
