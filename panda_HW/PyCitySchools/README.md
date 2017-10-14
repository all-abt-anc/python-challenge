

```python
import pandas as pd
import numpy as np
```


```python
schools_complete_csv_path = "raw_data/schools_complete.csv"
students_complete_csv_path = "raw_data/students_complete.csv"
```


```python
schools_complete_df = pd.read_csv(schools_complete_csv_path)
students_complete_df = pd.read_csv(students_complete_csv_path)
```


```python
#schools_complete_df
```


```python
#students_complete_df.head()
```


```python
total_budget = schools_complete_df['budget'].sum()
```


```python
total_schools = schools_complete_df['name'].count()
```


```python
total_students = students_complete_df['name'].count()
```


```python
average_math_score = students_complete_df['math_score'].mean()
average_reading_score = students_complete_df['reading_score'].mean()

```


```python
bins = [0, 70, 100]
group_names = ['Failed', 'Passed']
students_complete_df['reading_grade_status'] = pd.cut(students_complete_df["reading_score"], bins, labels=group_names)
students_complete_df['math_grade_status'] = pd.cut(students_complete_df["math_score"], bins, labels=group_names)
#students_complete_df['math_grade_status'].value_counts()['Passed']
percent_passing_math = ((students_complete_df['math_grade_status'].value_counts()['Passed'])/total_students) * 100
percent_passing_reading = ((students_complete_df['reading_grade_status'].value_counts()['Passed'])/total_students) * 100

```


```python
students_complete_df['overall_average_score'] = (students_complete_df['reading_score'] + students_complete_df['math_score'])/2
students_complete_df = students_complete_df[['Student ID', 'name', 'gender', 'grade', 'school', 'reading_score', 'reading_grade_status',
       'math_score', 'math_grade_status','overall_average_score']]
overall_passing_rate = (percent_passing_math + percent_passing_reading)/2
```


```python
#students_complete_df.head()
#students_complete_df["math_grade_status"].value_counts()
```


```python
district_summary_table = pd.DataFrame({"Total Schools":[total_schools],"Total Students":[total_students],
                                       "Total Budget":[total_budget],"Average Math Score":[average_math_score],
                                       "Average Reading Score":[average_reading_score],"% Passing Math":[percent_passing_math],
                                       "% Passing Reading":[percent_passing_reading],"Overall Passing Rate":[overall_passing_rate]})
district_summary_table = district_summary_table[["Total Schools","Total Students","Total Budget","Average Math Score","Average Reading Score","% Passing Math","% Passing Reading","Overall Passing Rate"]]

```


```python
district_summary_table

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>24649428</td>
      <td>78.985371</td>
      <td>81.87784</td>
      <td>72.392137</td>
      <td>82.971662</td>
      <td>77.681899</td>
    </tr>
  </tbody>
</table>
</div>




```python
schools_complete_df = schools_complete_df.rename(columns={"name":"school"})
#schools_complete_df
```


```python
merge_schools_student_table_df = pd.merge(schools_complete_df, students_complete_df, on="school", how="left")
#merge_schools_student_table_df.head()
```


```python
total_students_count_per_school = merge_schools_student_table_df["school"].value_counts()
school_summary_total_students_df = pd.DataFrame(total_students_count_per_school)
school_summary_total_students_df.reset_index(inplace=True)
school_summary_total_students_df.columns = ["School Name", "Total Students"]
```


```python
#school_summary_total_students_df
```


```python
schools_complete_school_rename_df = schools_complete_df.rename(columns={"school":"School Name"})
school_summary_merge1_df = pd.merge(schools_complete_school_rename_df, school_summary_total_students_df, on="School Name")
school_summary_merge1_df = school_summary_merge1_df.rename(columns={"budget":"Total School Budget", "type":"School Type"})
school_summary_merge1_df["Per Student Budget"] = (school_summary_merge1_df ["Total School Budget"] / school_summary_merge1_df ["Total Students"])
school_summary_merge1_df = school_summary_merge1_df[["School Name","School Type","Total Students","Total School Budget","Per Student Budget"]]
#school_summary_merge1_df
```


```python
grouped_by_school_total_rading_math_score_df = pd.DataFrame(merge_schools_student_table_df.groupby("school")["reading_score","math_score"].sum())
grouped_by_school_total_rading_math_score_df.reset_index(inplace=True)
grouped_by_school_total_rading_math_score_df.columns=["school", "reading_score","math_score"]
grouped_by_school_total_rading_math_score_df = grouped_by_school_total_rading_math_score_df.rename(columns={"school":"School Name"})
#grouped_by_school_total_rading_math_score_df
school_student_summary_per_school_merge2_df = pd.merge(school_summary_total_students_df, grouped_by_school_total_rading_math_score_df, on="School Name")
school_student_summary_per_school_merge2_df
school_student_summary_per_school_merge2_df ["Average Math Score"] = school_student_summary_per_school_merge2_df ["math_score"] / school_student_summary_per_school_merge2_df["Total Students"]
school_student_summary_per_school_merge2_df ["Average Reading Score"] = school_student_summary_per_school_merge2_df ["reading_score"] / school_student_summary_per_school_merge2_df["Total Students"]
school_student_summary_per_school_merge2_df
school_student_summary_per_school_merge2_df = school_student_summary_per_school_merge2_df[["School Name", "Average Math Score","Average Reading Score"]]
#school_student_summary_per_school_merge2_df
```


```python
school_summary_merge3_df = pd.merge(school_summary_merge1_df, school_student_summary_per_school_merge2_df, on="School Name")
#school_summary_merge3_df
```


```python
students_complete_reading_passed_df = students_complete_df.loc[students_complete_df["reading_grade_status"] == "Passed",:]
students_complete_reading_passed_df = students_complete_reading_passed_df [["school","reading_grade_status"]]
students_complete_reading_passed_per_school_df = students_complete_reading_passed_df["school"].value_counts()
students_complete_reading_passed_per_school_df = pd.DataFrame(students_complete_reading_passed_per_school_df)
students_complete_reading_passed_per_school_df.reset_index(inplace=True)
students_complete_reading_passed_per_school_df.columns = ["School Name", "Total Passing Reading"]
students_complete_reading_passed_per_school_df 
school_student_summary_per_school_merge4_df = pd.merge(school_summary_total_students_df, students_complete_reading_passed_per_school_df, on="School Name")
school_student_summary_per_school_merge4_df["% Passing Reading"] = (school_student_summary_per_school_merge4_df["Total Passing Reading"] / school_student_summary_per_school_merge4_df["Total Students"]) * 100
#school_student_summary_per_school_merge4_df
school_student_summary_per_school_merge4_df = school_student_summary_per_school_merge4_df [["School Name","% Passing Reading"]]
#school_student_summary_per_school_merge4_df
```


```python
school_summary_merge5_df = pd.merge(school_summary_merge3_df, school_student_summary_per_school_merge4_df, on="School Name")
#school_summary_merge5_df
```


```python
students_complete_math_passed_df = students_complete_df.loc[students_complete_df["math_grade_status"] == "Passed",:]
students_complete_math_passed_df = students_complete_math_passed_df [["school","math_grade_status"]]
students_complete_math_passed_per_school_df = students_complete_math_passed_df["school"].value_counts()
students_complete_math_passed_per_school_df = pd.DataFrame(students_complete_math_passed_per_school_df)
students_complete_math_passed_per_school_df.reset_index(inplace=True)
students_complete_math_passed_per_school_df.columns = ["School Name", "Total Passing Math"]
#students_complete_math_passed_per_school_df 
school_student_summary_per_school_merge6_df = pd.merge(school_summary_total_students_df, students_complete_math_passed_per_school_df, on="School Name")
school_student_summary_per_school_merge6_df["% Passing Math"] = (school_student_summary_per_school_merge6_df["Total Passing Math"] / school_student_summary_per_school_merge6_df["Total Students"]) * 100
#school_student_summary_per_school_merge6_df
school_student_summary_per_school_merge6_df = school_student_summary_per_school_merge6_df [["School Name","% Passing Math"]]
#school_student_summary_per_school_merge6_df
```


```python
school_summary_merge7_df = pd.merge(school_summary_merge5_df, school_student_summary_per_school_merge6_df, on="School Name")
#school_summary_merge7_df
```


```python
school_summary_merge7_df["Overall Passing Rate"] = (school_summary_merge7_df["% Passing Reading"] + school_summary_merge7_df["% Passing Math"]) / 2
#school_summary_merge7_df
```


```python
final_school_summary_merge7_index_df = school_summary_merge7_df.set_index("School Name")
final_school_summary_merge7_index_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>78.813850</td>
      <td>63.318478</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>78.433367</td>
      <td>63.750424</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>92.617831</td>
      <td>89.892107</td>
      <td>91.254969</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>78.187702</td>
      <td>64.746494</td>
      <td>71.467098</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>89.713896</td>
      <td>91.553134</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.254490</td>
      <td>90.932983</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>93.864370</td>
      <td>89.558665</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>79.300643</td>
      <td>64.630225</td>
      <td>71.965434</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.740047</td>
      <td>90.632319</td>
      <td>91.686183</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>92.203742</td>
      <td>91.683992</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.444444</td>
      <td>90.277778</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>77.744436</td>
      <td>64.066017</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>78.281874</td>
      <td>63.852132</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>77.510040</td>
      <td>65.753925</td>
      <td>71.631982</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>92.905199</td>
      <td>90.214067</td>
      <td>91.559633</td>
    </tr>
  </tbody>
</table>
</div>




```python
#final_school_summary_merge7_index_df["Average Math Score"] = final_school_summary_merge7_index_df["Average Math Score"].map("{0:,.2f}%".format)
#final_school_summary_merge7_index_df["Average Reading Score"] = final_school_summary_merge7_index_df["Average Reading Score"].map("{0:,.2f}%".format)
#final_school_summary_merge7_index_df["% Passing Reading"] = final_school_summary_merge7_index_df["% Passing Reading"].map("{0:,.2f}%".format)
#final_school_summary_merge7_index_df["% Passing Math"] = final_school_summary_merge7_index_df["% Passing Math"].map("{0:,.2f}%".format)
#final_school_summary_merge7_index_df["Overall Passing Rate"] = final_school_summary_merge7_index_df["Overall Passing Rate"].map("{0:,.2f}%".format)
#final_school_summary_merge7_index_df
```


```python
top_school_summary_merge7_index_df = final_school_summary_merge7_index_df.sort_values("Overall Passing Rate", ascending=False)
top_school_summary_merge7_index_df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Wilson High School</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.254490</td>
      <td>90.932983</td>
      <td>92.093736</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>92.203742</td>
      <td>91.683992</td>
      <td>91.943867</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.444444</td>
      <td>90.277778</td>
      <td>91.861111</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>93.864370</td>
      <td>89.558665</td>
      <td>91.711518</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.740047</td>
      <td>90.632319</td>
      <td>91.686183</td>
    </tr>
  </tbody>
</table>
</div>




```python
bottom_school_summary_merge7_index_df = final_school_summary_merge7_index_df.sort_values("Overall Passing Rate", ascending=True)
bottom_school_summary_merge7_index_df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rodriguez High School</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>77.744436</td>
      <td>64.066017</td>
      <td>70.905226</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>78.813850</td>
      <td>63.318478</td>
      <td>71.066164</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>78.281874</td>
      <td>63.852132</td>
      <td>71.067003</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>78.433367</td>
      <td>63.750424</td>
      <td>71.091896</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>78.187702</td>
      <td>64.746494</td>
      <td>71.467098</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_scores_by_grade_merge_schools_student_table_df = merge_schools_student_table_df[["school","grade","math_score" ]]
math_scores_by_grade_merge_schools_student_table_df = math_scores_by_grade_merge_schools_student_table_df.rename(columns={"school":"School Name"})
#math_scores_by_grade_merge_schools_student_table_df["grade"].value_counts()

```


```python
math_scores_by_grade_merge_schools_student_table_9th_df = math_scores_by_grade_merge_schools_student_table_df.loc[math_scores_by_grade_merge_schools_student_table_df["grade"] == "9th"]
#math_scores_by_grade_merge_schools_student_table_9th_df
grouped_by_math_scores_by_grade_merge_schools_student_table_9th_df = pd.DataFrame(math_scores_by_grade_merge_schools_student_table_9th_df.groupby("School Name")["math_score"].mean())
grouped_by_math_scores_by_grade_merge_schools_student_table_9th_df.reset_index(inplace=True)
grouped_by_math_scores_by_grade_merge_schools_student_table_9th_df =grouped_by_math_scores_by_grade_merge_schools_student_table_9th_df.rename(columns={"math_score":"9th"})
#grouped_by_math_scores_by_grade_merge_schools_student_table_9th_df


math_scores_by_grade_merge_schools_student_table_10th_df = math_scores_by_grade_merge_schools_student_table_df.loc[math_scores_by_grade_merge_schools_student_table_df["grade"] == "10th"]
#math_scores_by_grade_merge_schools_student_table_10th_df
grouped_by_math_scores_by_grade_merge_schools_student_table_10th_df = pd.DataFrame(math_scores_by_grade_merge_schools_student_table_10th_df.groupby("School Name")["math_score"].mean())
grouped_by_math_scores_by_grade_merge_schools_student_table_10th_df.reset_index(inplace=True)
grouped_by_math_scores_by_grade_merge_schools_student_table_10th_df =grouped_by_math_scores_by_grade_merge_schools_student_table_10th_df.rename(columns={"math_score":"10th"})
#grouped_by_math_scores_by_grade_merge_schools_student_table_10th_df

math_scores_by_grade_merge_schools_student_table_11th_df = math_scores_by_grade_merge_schools_student_table_df.loc[math_scores_by_grade_merge_schools_student_table_df["grade"] == "11th"]
#math_scores_by_grade_merge_schools_student_table_11th_df
grouped_by_math_scores_by_grade_merge_schools_student_table_11th_df = pd.DataFrame(math_scores_by_grade_merge_schools_student_table_11th_df.groupby("School Name")["math_score"].mean())
grouped_by_math_scores_by_grade_merge_schools_student_table_11th_df.reset_index(inplace=True)
grouped_by_math_scores_by_grade_merge_schools_student_table_11th_df =grouped_by_math_scores_by_grade_merge_schools_student_table_11th_df.rename(columns={"math_score":"11th"})
#grouped_by_math_scores_by_grade_merge_schools_student_table_11th_df


math_scores_by_grade_merge_schools_student_table_12th_df = math_scores_by_grade_merge_schools_student_table_df.loc[math_scores_by_grade_merge_schools_student_table_df["grade"] == "12th"]
#math_scores_by_grade_merge_schools_student_table_12th_df
grouped_by_math_scores_by_grade_merge_schools_student_table_12th_df = pd.DataFrame(math_scores_by_grade_merge_schools_student_table_12th_df.groupby("School Name")["math_score"].mean())
grouped_by_math_scores_by_grade_merge_schools_student_table_12th_df.reset_index(inplace=True)
grouped_by_math_scores_by_grade_merge_schools_student_table_12th_df =grouped_by_math_scores_by_grade_merge_schools_student_table_12th_df.rename(columns={"math_score":"12th"})
#grouped_by_math_scores_by_grade_merge_schools_student_table_12th_df

```


```python
math_scores_by_grade_1st_half_df = pd.merge(grouped_by_math_scores_by_grade_merge_schools_student_table_9th_df, 
                                grouped_by_math_scores_by_grade_merge_schools_student_table_10th_df,  on="School Name")


math_scores_by_grade_2nd_half_df = pd.merge(grouped_by_math_scores_by_grade_merge_schools_student_table_11th_df,
                                grouped_by_math_scores_by_grade_merge_schools_student_table_12th_df, on="School Name")

math_scores_by_grade_df = pd.merge(math_scores_by_grade_1st_half_df,math_scores_by_grade_2nd_half_df, on="School Name")
math_scores_by_grade_df = math_scores_by_grade_df.set_index("School Name")
math_scores_by_grade_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading_scores_by_grade_merge_schools_student_table_df = merge_schools_student_table_df[["school","grade","reading_score" ]]
reading_scores_by_grade_merge_schools_student_table_df = reading_scores_by_grade_merge_schools_student_table_df.rename(columns={"school":"School Name"})
#reading_scores_by_grade_merge_schools_student_table_df

```


```python
reading_scores_by_grade_merge_schools_student_table_9th_df = reading_scores_by_grade_merge_schools_student_table_df.loc[reading_scores_by_grade_merge_schools_student_table_df["grade"] == "9th"]
#reading_scores_by_grade_merge_schools_student_table_9th_df
grouped_by_reading_scores_by_grade_merge_schools_student_table_9th_df = pd.DataFrame(reading_scores_by_grade_merge_schools_student_table_9th_df.groupby("School Name")["reading_score"].mean())
grouped_by_reading_scores_by_grade_merge_schools_student_table_9th_df.reset_index(inplace=True)
grouped_by_reading_scores_by_grade_merge_schools_student_table_9th_df =grouped_by_reading_scores_by_grade_merge_schools_student_table_9th_df.rename(columns={"reading_score":"9th"})
#grouped_by_reading_scores_by_grade_merge_schools_student_table_9th_df


reading_scores_by_grade_merge_schools_student_table_10th_df = reading_scores_by_grade_merge_schools_student_table_df.loc[reading_scores_by_grade_merge_schools_student_table_df["grade"] == "10th"]
#reading_scores_by_grade_merge_schools_student_table_10th_df
grouped_by_reading_scores_by_grade_merge_schools_student_table_10th_df = pd.DataFrame(reading_scores_by_grade_merge_schools_student_table_10th_df.groupby("School Name")["reading_score"].mean())
grouped_by_reading_scores_by_grade_merge_schools_student_table_10th_df.reset_index(inplace=True)
grouped_by_reading_scores_by_grade_merge_schools_student_table_10th_df =grouped_by_reading_scores_by_grade_merge_schools_student_table_10th_df.rename(columns={"reading_score":"10th"})
#grouped_by_reading_scores_by_grade_merge_schools_student_table_10th_df

reading_scores_by_grade_merge_schools_student_table_11th_df = reading_scores_by_grade_merge_schools_student_table_df.loc[reading_scores_by_grade_merge_schools_student_table_df["grade"] == "11th"]
#reading_scores_by_grade_merge_schools_student_table_11th_df
grouped_by_reading_scores_by_grade_merge_schools_student_table_11th_df = pd.DataFrame(reading_scores_by_grade_merge_schools_student_table_11th_df.groupby("School Name")["reading_score"].mean())
grouped_by_reading_scores_by_grade_merge_schools_student_table_11th_df.reset_index(inplace=True)
grouped_by_reading_scores_by_grade_merge_schools_student_table_11th_df =grouped_by_reading_scores_by_grade_merge_schools_student_table_11th_df.rename(columns={"reading_score":"11th"})
#grouped_by_reading_scores_by_grade_merge_schools_student_table_11th_df


reading_scores_by_grade_merge_schools_student_table_12th_df = reading_scores_by_grade_merge_schools_student_table_df.loc[reading_scores_by_grade_merge_schools_student_table_df["grade"] == "12th"]
#reading_scores_by_grade_merge_schools_student_table_12th_df
grouped_by_reading_scores_by_grade_merge_schools_student_table_12th_df = pd.DataFrame(reading_scores_by_grade_merge_schools_student_table_12th_df.groupby("School Name")["reading_score"].mean())
grouped_by_reading_scores_by_grade_merge_schools_student_table_12th_df.reset_index(inplace=True)
grouped_by_reading_scores_by_grade_merge_schools_student_table_12th_df =grouped_by_reading_scores_by_grade_merge_schools_student_table_12th_df.rename(columns={"reading_score":"12th"})
#grouped_by_reading_scores_by_grade_merge_schools_student_table_12th_df
```


```python
reading_scores_by_grade_1st_half_df = pd.merge(grouped_by_reading_scores_by_grade_merge_schools_student_table_9th_df, 
                                grouped_by_reading_scores_by_grade_merge_schools_student_table_10th_df,  on="School Name")


reading_scores_by_grade_2nd_half_df = pd.merge(grouped_by_reading_scores_by_grade_merge_schools_student_table_11th_df,
                                grouped_by_reading_scores_by_grade_merge_schools_student_table_12th_df, on="School Name")

reading_scores_by_grade_df = pd.merge(reading_scores_by_grade_1st_half_df,reading_scores_by_grade_2nd_half_df, on="School Name")
reading_scores_by_grade_df = reading_scores_by_grade_df.set_index("School Name")
reading_scores_by_grade_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
    <tr>
      <th>School Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>




```python
final_school_summary_merge7_index_2nd_copy_df = final_school_summary_merge7_index_df
#final_school_summary_merge7_index_2nd_copy_df

```


```python
final_school_summary_merge7_index_2nd_copy_df.reset_index(inplace=True)
final_school_summary_merge7_index_per_student_spending_df = final_school_summary_merge7_index_2nd_copy_df [["Per Student Budget", "Average Math Score", "Average Reading Score","% Passing Reading", "% Passing Math", "Overall Passing Rate"]]
#final_school_summary_merge7_index_per_student_spending_df

```


```python
bins = [500, 585, 600, 625, 660]
group_names = ['<$585', '$585-$600', '$600-$625', '$625-$660']
```


```python
final_school_summary_merge7_index_per_student_spending_df["Spending Ranges (Per Student)"] = pd.cut(final_school_summary_merge7_index_per_student_spending_df["Per Student Budget"], bins, labels=group_names)
#final_school_summary_merge7_index_per_student_spending_df

```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.



```python
final_school_summary_merge7_index_per_student_spending_df = final_school_summary_merge7_index_per_student_spending_df [["Spending Ranges (Per Student)","Average Math Score","Average Reading Score","% Passing Reading","% Passing Math","Overall Passing Rate"]]
#final_school_summary_merge7_index_per_student_spending_df
```


```python
grouped_by_final_school_summary_merge7_index_per_student_spending_df = pd.DataFrame(final_school_summary_merge7_index_per_student_spending_df.groupby("Spending Ranges (Per Student)")["Average Math Score","Average Reading Score","% Passing Reading","% Passing Math","Overall Passing Rate"].sum())
grouped_by_final_school_summary_merge7_index_per_student_spending_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spending Ranges (Per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$585</th>
      <td>333.821596</td>
      <td>335.735256</td>
      <td>373.303351</td>
      <td>361.401744</td>
      <td>367.352548</td>
    </tr>
    <tr>
      <th>$585-$600</th>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>92.617831</td>
      <td>89.892107</td>
      <td>91.254969</td>
    </tr>
    <tr>
      <th>$600-$625</th>
      <td>167.191415</td>
      <td>167.861456</td>
      <td>185.596113</td>
      <td>181.397888</td>
      <td>183.497000</td>
    </tr>
    <tr>
      <th>$625-$660</th>
      <td>622.115480</td>
      <td>650.615384</td>
      <td>641.177111</td>
      <td>540.331761</td>
      <td>590.754436</td>
    </tr>
  </tbody>
</table>
</div>




```python
final_school_summary_merge7_index_school_size_df = final_school_summary_merge7_index_2nd_copy_df [["Total Students", "Average Math Score", "Average Reading Score","% Passing Reading", "% Passing Math", "Overall Passing Rate"]]
#final_school_summary_merge7_index_school_size_df
```


```python
bins = [100, 1000, 3000, 5000]
group_names = ['Small(<1000)', 'Medium(1000-3000)', 'Large(3000-5000)']
```


```python
final_school_summary_merge7_index_school_size_df["School Size"] = pd.cut(final_school_summary_merge7_index_school_size_df["Total Students"], bins, labels=group_names)
#final_school_summary_merge7_index_school_size_df


```

    /anaconda3/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      """Entry point for launching an IPython kernel.



```python
final_school_summary_merge7_index_school_size_df = final_school_summary_merge7_index_school_size_df [["School Size","Average Math Score","Average Reading Score","% Passing Reading","% Passing Math","Overall Passing Rate"]]
#final_school_summary_merge7_index_school_size_df
```


```python
grouped_by_final_school_summary_merge7_index_school_size_df = pd.DataFrame(final_school_summary_merge7_index_school_size_df.groupby("School Size")["Average Math Score","Average Reading Score","% Passing Reading","% Passing Math","Overall Passing Rate"].sum())
grouped_by_final_school_summary_merge7_index_school_size_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small(&lt;1000)</th>
      <td>167.643196</td>
      <td>167.859687</td>
      <td>184.943789</td>
      <td>182.316310</td>
      <td>183.630050</td>
    </tr>
    <tr>
      <th>Medium(1000-3000)</th>
      <td>730.591392</td>
      <td>746.398679</td>
      <td>794.235962</td>
      <td>733.412323</td>
      <td>763.824142</td>
    </tr>
    <tr>
      <th>Large(3000-5000)</th>
      <td>308.253359</td>
      <td>323.679455</td>
      <td>313.514655</td>
      <td>257.294868</td>
      <td>285.404761</td>
    </tr>
  </tbody>
</table>
</div>




```python
final_school_summary_merge7_index_school_type_df = final_school_summary_merge7_index_2nd_copy_df [["School Type", "Average Math Score", "Average Reading Score","% Passing Reading", "% Passing Math", "Overall Passing Rate"]]
#final_school_summary_merge7_index_school_type_df
```


```python
grouped_by_final_school_summary_merge7_index_school_type_df = pd.DataFrame(final_school_summary_merge7_index_school_type_df.groupby("School Type")["Average Math Score","Average Reading Score","% Passing Reading","% Passing Math","Overall Passing Rate"].sum())
grouped_by_final_school_summary_merge7_index_school_type_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Reading</th>
      <th>% Passing Math</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>667.790815</td>
      <td>671.171366</td>
      <td>744.422494</td>
      <td>722.905807</td>
      <td>733.664150</td>
    </tr>
    <tr>
      <th>District</th>
      <td>538.697131</td>
      <td>566.766454</td>
      <td>548.271912</td>
      <td>450.117694</td>
      <td>499.194803</td>
    </tr>
  </tbody>
</table>
</div>


