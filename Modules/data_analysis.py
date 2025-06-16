from data_loading import data_load
from data_cleaning import cleaning
from data_visualization import visualization

def main():
    df=data_load("retail_store.csv")

    df=cleaning(df,"Price")

    visualization(df,"Product","Price")

    return df

if __name__=="__main__":
    main()