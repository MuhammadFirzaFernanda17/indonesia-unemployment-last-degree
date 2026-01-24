#!/usr/bin/env python
# coding: utf-8

# In[2]:


#mengimport 3 paket utama
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import streamlit as st
from datetime import datetime, timedelta


# In[3]:


#memasukkan dan menampilkan dataset
df = pd.read_csv('dataset/Data Training-1.csv')
df


# In[4]:


df.isnull().sum()


# In[5]:


df.describe(include='all')


# In[6]:


# Exploratory Data Analysis (EDA)
mean_cnt_by_belum_sekolah = df['Tidak/belum pernah sekolah'].mean()
mean_cnt_by_belum_sd = df['Tidak/belum tamat SD'].mean()
mean_cnt_by_sd = df['SD'].mean()
mean_cnt_by_smp = df['SLTP'].mean()

mean_cnt_by_sma = df['SLTA Umum/SMU'].mean()
mean_cnt_by_smk = df['SLTA Kejuruan/SMK'].mean()

mean_cnt_by_diploma = df['Akademi/Diploma'].mean()
mean_cnt_by_sarjana = df['Universitas'].mean()


# In[7]:


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
        mean_cnt_by_belum_sekolah,
        mean_cnt_by_belum_sd,
        mean_cnt_by_sd,
        mean_cnt_by_smp,
        mean_cnt_by_sma,
        mean_cnt_by_smk,
        mean_cnt_by_diploma,
        mean_cnt_by_sarjana
    ]
})

mean_education_df


# In[8]:


plt.figure(figsize=(10, 6))
sns.barplot(data=mean_education_df,
    x="Tingkat Pendidikan",
    hue="Tingkat Pendidikan",
    y="Rata-rata Jumlah Penduduk",
    palette="magma"
)
plt.xticks(rotation=35, ha="right")
plt.title("Rata-rata Jumlah Penduduk Berdasarkan Tingkat Pendidikan")
plt.ylabel("Rata-rata Jumlah Penduduk")
plt.tight_layout()
plt.show()


# In[ ]:


df.groupby('Periode')['Total'].mean().sort_values()


# In[ ]:


total_pengangguran_per_tahun = df.groupby('Periode')['Total'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.lineplot(data=total_pengangguran_per_tahun)
plt.plot(total_pengangguran_per_tahun.index, total_pengangguran_per_tahun.values)
plt.xlabel("Periode")
plt.ylabel("Total Pengangguran")
plt.title("Total Pengangguran Berdasarkan Periode")

