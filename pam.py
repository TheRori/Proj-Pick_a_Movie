from app import app
from senscritiquescraper import Senscritique
import pandas as pd


if __name__ == '__main__':
    user_collection = Senscritique.get_survey("https://www.senscritique.com/liste/Films_a_voir_ye/3005148")
    df_user_collection = pd.DataFrame(user_collection)
    df_user_collection = df_user_collection.drop(columns=['Rank','Description'])
    print(df_user_collection)
