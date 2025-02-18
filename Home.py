import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime

def main():
    
    st.title("従業員数ランク(Ｂ以上)。")
    uploaded_file = st.file_uploader("エクセルファイルをアップロード", type=["xlsx","xls"])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.header("アップロードしたデータ:")

        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  
        df.to_csv(f"data_{now}.csv", index=False)
        if set(df.columns) == set(["スナップショット日","GA企業担当者","GA企業担当者部署","取引先: 企業名","従業員数ランク","TG在籍人数"]):
            st.write("データは正しい形式です。")
        else:
            st.write("データ形式が正しくありません。正しいデータをアップロードしてください。")

        df["スナップショット日"] = pd.to_datetime(df["スナップショット日"])
        df["スナップショット月"] = df["スナップショット日"].dt.strftime("%Y-%m")

        if set(df.columns) == set(["スナップショット日","GA企業担当者","GA企業担当者部署","取引先: 企業名","従業員数ランク","TG在籍人数","スナップショット月"]):
            pivot = df.pivot_table(index=["GA企業担当者部署","GA企業担当者"],columns=["従業員数ランク"],values="スナップショット日",aggfunc="count",fill_value=0)
            pivot = pivot.sort_values(by="GA企業担当者部署",ascending=False)
            st.header("GA企業担当者部署ごとのデータ数:")
            st.dataframe(pivot)
            selected = st.sidebar.selectbox("GA企業担当者部署を選んでください", pivot.index.get_level_values(0).unique())
            st.write(f"{selected}のデータ:")
            st.dataframe(pivot.loc[selected])
            plt.rcParams['font.family'] = "MS Gothic"
            fig, ax = plt.subplots()
            pivot.loc[selected].plot(kind="bar",ax=ax)

            table = ax.table(cellText=pivot.loc[selected].values,
                             rowLabels=pivot.loc[selected].index,
                             colLabels=pivot.columns,
                             loc='top')

            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1.2, 1.2)
            st.pyplot(fig)

if __name__ == "__main__":
    main()