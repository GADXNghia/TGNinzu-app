# FILE: /streamlit-app/streamlit-app/Home.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as datetime

def main():
    
    st.title("従業員数ランク(Ｂ以上)")
    ### ask user to upload an excel file
    uploaded_file = st.file_uploader("エクセルファイルをアップロード", type=["xlsx","xls"])
    ### if file is uploaded, read the file and display the data summary, column names
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.header("アップロードしたデータ:")

        ### save the data to a csv file in the local directory without confirm with user, name the file as data"timestamp".csv
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  
        ### df.to_csv(f"data_{now}.csv", index=False)
        ### check if the dateframe only has the columns スナップショット日 GA企業担当者 GA企業担当者部署 取引先: 企業名 従業員数ランク TG在籍人数
        if set(df.columns) == set(["スナップショット日","GA企業担当者","GA企業担当者部署","取引先: 企業名","従業員数ランク","TG在籍人数"]):
            st.write("データは正しい形式です")
        ### if not ask the user to upload the correct file
        else:
            st.write("データ形式が正しくありません。正しいデータをアップロードしてください")

        ### convert "スナップショット月" into datetime
        df["スナップショット日"] = pd.to_datetime(df["スナップショット日"])
        # create a new column "スナップショット月" by extracting the month and year from the column "スナップショット日" for example 2021-11-01 will be 2021-11
        df["スナップショット月"] = df["スナップショット日"].dt.strftime("%Y-%m")

        st.dataframe(df.head())
        st.write("列名:")
        st.write(df.columns)        
        ### if the data is correct, create a pivot table count the row in each GA企業担当者部署 GA企業担当者 devide by スナップショット月, sort the table by GA企業担当者部署 and count, and save the table into dataframe "pivot" put the months in order 11, 12, 1
        if set(df.columns) == set(["スナップショット日","GA企業担当者","GA企業担当者部署","取引先: 企業名","従業員数ランク","TG在籍人数","スナップショット月"]):
            pivot = df.pivot_table(index=["GA企業担当者部署","GA企業担当者"],columns="スナップショット月",values="スナップショット日",aggfunc="count",fill_value=0)
            pivot = pivot.sort_values(by="GA企業担当者部署",ascending=False)
            st.header("GA企業担当者部署ごとのデータ数:")
            ### display the pivot table with column order of increasing month 
            st.dataframe(pivot)
            ### add a picker in the side bar to let user choose the multiple GA企業担当者部署 to display the data in the pivot table if it selected, hide the pivot table above and display the selected data
            selected = st.sidebar.selectbox("GA企業担当者部署を選んでください", pivot.index.get_level_values(0).unique())
            st.write(f"{selected}のデータ:")
            st.dataframe(pivot.loc[selected])
            # you matplotlib to format the table and display the data in the pivot table as a bar chart with the table at the bottom of the chart
            plt.rcParams['font.family'] = "MS Gothic"
            fig, ax = plt.subplots()
            pivot.loc[selected].plot(kind="bar",ax=ax)
            st.pyplot(fig)

if __name__ == "__main__":
    main()