"""Description:
This task involves performing exploratory
data analysis on a dataset.
Responsibility:
Create visualizations to understand the
distribution of variables, identify outliers,
and check for correlations between
variables."""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from datetime import datetime
from IPython.display import display
df=pd.read_csv("C:\\Users\\ASUS\\Downloads\\USvideos.csv")
#________1___________ 
display(df.head)
#________2___________ 
display(df.shape)
#________3___________ 
df = df.drop_duplicates()
print(df.shape)
#________4___________ 
display(df.describe)
#________5___________ 
print(df.info)
#________6___________
columns_to_remove = {'thumbnail_link', 'description'}
df = df.drop(columns=columns_to_remove)
df.info()
#________7___________ 
from datetime import datetime
import datetime
df["trending_date"] = df["trending_date"].apply(lambda x: datetime.datetime.strptime(x,'%y.%d.%m'))
print(df.head(5))
#________8___________ 
df['publish_time'] = pd.to_datetime(df['publish_time'])
print(df.head(3))
#_________9__________ 
import pandas as pd
try:
    df = pd.read_csv('USvideos.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
if 'publish_time' not in df.columns:
    print("The 'publish_time' column is not present in the dataset.")
else:
    try:
        df['publish_time'] = pd.to_datetime(df['publish_time'])
        df['publish_month'] = df['publish_time'].dt.month
        df['publish_day'] = df['publish_time'].dt.day
        df['publish_hour'] = df['publish_time'].dt.hour
        print(df.head(3))
    except Exception as e:
        print(f"An error occurred during processing: {e}")

#_________10__________ 
print(sorted(df['category_id'].unique()))
#________11___________ 
import numpy as np
df['category_name'] = np.nan
# Use .loc to assign category names based on 'category_id'
df.loc[df["category_id"] == 1, "category_name"] = 'Film and Animation'
df.loc[df["category_id"] == 2, "category_name"] = 'Autos and Vehicles'
df.loc[df["category_id"] == 10, "category_name"] = 'Music'
df.loc[df["category_id"] == 15, "category_name"] = 'Pets and Animals'
df.loc[df["category_id"] == 17, "category_name"] = 'Sports'
df.loc[df["category_id"] == 19, "category_name"] = 'Travel and Events'
df.loc[df["category_id"] == 20, "category_name"] = 'Gaming'
df.loc[df["category_id"] == 22, "category_name"] = 'People and Blogs'
df.loc[df["category_id"] == 23, "category_name"] = 'Comedy'
df.loc[df["category_id"] == 24, "category_name"] = 'Entertainment'
df.loc[df["category_id"] == 25, "category_name"] = 'News and Politics'
df.loc[df["category_id"] == 26, "category_name"] = 'How to and Style'
df.loc[df["category_id"] == 27, "category_name"] = 'Education'
df.loc[df["category_id"] == 28, "category_name"] = 'Science and Technology'
df.loc[df["category_id"] == 29, "category_name"] = 'Non Profits and Activism'
df.loc[df["category_id"] == 30, "category_name"] = 'Movies'
df.loc[df["category_id"] == 43, "category_name"] = 'Shows'
df.head()
#________12___________ 

df['publish_time'] = pd.to_datetime(df['publish_time'])
df['year'] = df['publish_time'].dt.year
yearly_counts = df.groupby('year')['video_id'].count()
# Create a bar chart
yearly_counts.plot(kind='bar', xlabel='Year', ylabel='Total Publish Count', title='Total Published Videos Per Year')
plt.show()

#________13___________ 
yearly_views = df.groupby('year')['views'].sum()
# Create a bar chart
yearly_views.plot(kind='bar', xlabel='Year', ylabel='Total views', title='Total views Per Year')
plt.xticks(rotation=0)
plt.tight_layout
plt.show()
#________14___________ 

category_views = df.groupby('category_name')['views'].sum().reset_index()
top_categories = category_views.sort_values(by='views', ascending=False).head(5)
plt.bar(top_categories['category_name'], top_categories['views'])
plt.xlabel('Category Name', fontsize=12)
plt.ylabel('Total Views', fontsize=12)  
plt.title('Top 5 Categories', fontsize=15)
plt.tight_layout()
plt.show()

#________15___________ 
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
sns.countplot(x='category_name', data=df, order=df['category_name'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Video Count by Category')
plt.show()

#________16______
videos_per_hour = df['publish_hour'].value_counts().sort_index().reset_index()
videos_per_hour.columns = ['publish_hour', 'count']
plt.figure(figsize=(12, 6))
sns.barplot(data=videos_per_hour, x='publish_hour', y='count', palette='rocket', hue='publish_hour', dodge=False, legend=False)
plt.title('Number of Videos Published per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()
#________17___________ 
df['publish_time'] = pd.to_datetime(df['publish_time'])
df['publish_date'] = df['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size().reset_index(name='count')
plt.figure(figsize=(12, 6))
sns.lineplot(x='publish_date', y='count', data=video_count_by_date)
plt.title("Videos Published Over Time")
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.show()
#________18___________ 
sns.scatterplot(data=df, x='views', y='likes')

plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')

plt.show()
#________19___________ 
plt.figure(figsize=(14, 8))
plt.subplots_adjust(wspace=0.2, hspace=0.4, top=0.9)

plt.subplot(2, 2, 1)
g = sns.countplot(x='comments_disabled', data=df)
g.set_title("Comments Disabled", fontsize=16)

plt.subplot(2, 2, 2)
g1 = sns.countplot(x='ratings_disabled', data=df)
g1.set_title("Rating Disabled", fontsize=16)

plt.subplot(2, 2, 3)
g2 = sns.countplot(x='video_error_or_removed', data=df)
g2.set_title("Video Error or Removed", fontsize=16)

plt.show()
#_____________20_______
corr_matrix = df['views'].corr(df['likes'])
print(corr_matrix)