#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="Dashboard Analisis Pendidikan",
    layout="wide"
)

st.title("📊 Dashboard Analisis Data Pendidikan & Pengangguran")

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    return pd.read_csv("dataset/Data Training-1.csv")

df = load_data()

st.subheader("Preview Dataset")
st.dataframe(df.head())

# ===============================
# DATA QUALITY CHECK
# ===============================
st.subheader("Cek Missing Value")
st.dataframe(df.isnull().sum())

st.subheader("Statistik Deskriptif")
st.dataframe(df.describe(include="all"))

# ===============================
# EDA - Rata-rata Pendidikan
# ===============================
st.subheader("Rata-rata Jumlah Penduduk Berdasarkan Tingkat Pendidikan")

mean_education_df = pd.DataFrame({
    "Tingkat Pendidikan": [
        "Tidak/belum pernah sekolah",
        "Tidak/belum tamat SD",
        "SD",
        "SMP",
        "SMA",
        "SMK",
        "Akademi/Diploma",
        "Universitas"
    ],
    "Rata-rata Jumlah Penduduk": [
        df['Tidak/belum pernah sekolah'].mean(),
        df['Tidak/belum tamat SD'].mean(),
        df['SD'].mean(),
        df['SLTP'].mean(),
        df['SLTA Umum/SMU'].mean(),
        df['SLTA Kejuruan/SMK'].mean(),
        df['Akademi/Diploma'].mean(),
        df['Universitas'].mean()
    ]
})

st.dataframe(mean_education_df)

# Plot Bar Chart
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(
    data=mean_education_df,
    x="Tingkat Pendidikan",
    y="Rata-rata Jumlah Penduduk",
    palette="magma",
    ax=ax1
)
plt.xticks(rotation=35, ha="right")
plt.title("Rata-rata Jumlah Penduduk Berdasarkan Tingkat Pendidikan")
plt.tight_layout()

st.pyplot(fig1)

# ===============================
# Total Pengangguran per Periode
# ===============================
st.subheader("Total Pengangguran Berdasarkan Periode")

total_pengangguran_per_tahun = (
    df.groupby('Periode')['Total']
    .mean()
    .sort_index()
)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(
    x=total_pengangguran_per_tahun.index,
    y=total_pengangguran_per_tahun.values,
    ax=ax2
)
plt.xlabel("Periode")
plt.ylabel("Total Pengangguran")
plt.title("Trend Total Pengangguran")
plt.tight_layout()

st.pyplot(fig2)

st.success("Dashboard berhasil dijalankan 🚀")