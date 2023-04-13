import pandas as pd

pd.set_option('display.max_columns', None) # hiển thị tất cả cột
pd.set_option('display.width', None) # giới hạn chiều rộng của frame để đảm bảo hiển thị đủ cột
pd.set_option('display.max_rows', None) # hiển thị tất cả dòng
pd.set_option("display.expand_frame_repr", False)

books = pd.read_csv('archive/Books.csv')
rating = pd.read_csv('archive/Ratings.csv')

df = rating.merge(books, how="left", on="ISBN")
df.head()
df.info()