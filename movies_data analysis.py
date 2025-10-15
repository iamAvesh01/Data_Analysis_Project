[Running] python -u "c:\Users\bcs\.vscode\tempCodeRunnerFile.python"
  Release_Date  ...                                         Poster_Url
0   2021-12-15  ...  https://image.tmdb.org/t/p/original/1g0dhYtq4i...
1   2022-03-01  ...  https://image.tmdb.org/t/p/original/74xTEgt7R3...
2   2022-02-25  ...  https://image.tmdb.org/t/p/original/vDHsLnOWKl...
3   2021-11-24  ...  https://image.tmdb.org/t/p/original/4j0PNHkMr5...
4   2021-12-22  ...  https://image.tmdb.org/t/p/original/aq4Pwv5Xeu...

[5 rows x 9 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9827 entries, 0 to 9826
Data columns (total 9 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Release_Date       9827 non-null   object 
 1   Title              9827 non-null   object 
 2   Overview           9827 non-null   object 
 3   Popularity         9827 non-null   float64
 4   Vote_Count         9827 non-null   int64  
 5   Vote_Average       9827 non-null   float64
 6   Original_Language  9827 non-null   object 
 7   Genre              9827 non-null   object 
 8   Poster_Url         9827 non-null   object 
dtypes: float64(2), int64(1), object(6)
memory usage: 691.1+ KB
None
0    Action, Adventure, Science Fiction
1              Crime, Mystery, Thriller
2                              Thriller
3    Animation, Comedy, Family, Fantasy
4      Action, Adventure, Thriller, War
Name: Genre, dtype: object
0
        Popularity    Vote_Count  Vote_Average
count  9827.000000   9827.000000   9827.000000
mean     40.326088   1392.805536      6.439534
std     108.873998   2611.206907      1.129759
min      13.354000      0.000000      0.000000
25%      16.128500    146.000000      5.900000
50%      21.199000    444.000000      6.500000
75%      35.191500   1376.000000      7.100000
max    5083.954000  31077.000000     10.000000
datetime64[ns]
int32
Index(['Release_Date', 'Title', 'Popularity', 'Vote_Count', 'Vote_Average',
       'Genre'],
      dtype='object')
['papular', 'below_avg', 'average', 'not_papular', NaN]
Categories (4, object): ['not_papular' < 'below_avg' < 'average' < 'papular']
   Release_Date  ...                               Genre
0          2021  ...  Action, Adventure, Science Fiction
1          2022  ...            Crime, Mystery, Thriller
2          2022  ...                            Thriller
3          2021  ...  Animation, Comedy, Family, Fantasy
4          2021  ...    Action, Adventure, Thriller, War

[5 rows x 6 columns]
Vote_Average
not_papular    2467
papular        2450
average        2412
below_avg      2398
Name: count, dtype: int64
Release_Date    0
Title           0
Popularity      0
Vote_Count      0
Vote_Average    0
Genre           0
dtype: int64
   Release_Date                    Title  ...  Vote_Average            Genre
0          2021  Spider-Man: No Way Home  ...       papular           Action
1          2021  Spider-Man: No Way Home  ...       papular        Adventure
2          2021  Spider-Man: No Way Home  ...       papular  Science Fiction
3          2022               The Batman  ...       papular            Crime
4          2022               The Batman  ...       papular          Mystery

[5 rows x 6 columns]
category
Release_Date     100
Title           9415
Popularity      8088
Vote_Count      3265
Vote_Average       4
Genre             19
dtype: int64
count     25552
unique       19
top       Drama
freq       3715
Name: Genre, dtype: object
   Release_Date                    Title  ...  Vote_Average            Genre
0          2021  Spider-Man: No Way Home  ...       papular           Action
1          2021  Spider-Man: No Way Home  ...       papular        Adventure
2          2021  Spider-Man: No Way Home  ...       papular  Science Fiction

[3 rows x 6 columns]
       Release_Date  ...            Genre
25546          2021  ...            Music
25547          2021  ...            Drama
25548          2021  ...          History
25549          1984  ...              War
25550          1984  ...            Drama
25551          1984  ...  Science Fiction

[6 rows x 6 columns]
Axes(0.125,0.11;0.775x0.77)

[Done] exited with code=0 in 109.58 seconds

