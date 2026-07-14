# Phase 1: Data Analysis of Student Data
import pandas as pd

# CSV file read
df = pd.read_csv("student_data.csv")

# First 5 rows show
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df["Math"].mean())
print(df["Math"].max())
topper= df.loc[df["Math"]== df["Math"].max()]
print(topper)
print(df["Science"].mean())
print(df["Science"].max())
topper= df.loc[df["Science"]== df["Science"].max()]
print(topper)
delhi_students= df.loc[df["City"]== "Delhi"]
print(delhi_students)
print(df["City"].value_counts())
female_Students=df.loc[df["Gender"]== "Female"]
print(female_Students)
print(female_Students.shape)
male_Students=df.loc[df["Gender"]== "Male"]
print(male_Students)
print(male_Students.shape)
high_math = df[df["Math"] > 80]
print(high_math)
high_Students_delhi=df.loc[(df["Math"] > 80) & (df["City"]== "Delhi")]
print(high_Students_delhi)
# Phase 2: Data Visualization of Student Data
import matplotlib.pyplot as plt
city_counts = df["City"].value_counts()
city_counts.plot(kind="bar")
plt.title("Number of Students in Each City")
plt.xlabel("City")
plt.ylabel("Number of Students")
plt.show()

plt.figure(figsize=(10, 6))
city_counts = df["City"].value_counts()
plt.pie(city_counts, labels=city_counts.index, autopct="%1.1f%%")
plt.title("Students Distribution by City")
plt.show()

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

plt.plot(df["Name"], df["Math"], marker="o")

plt.title("Math Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Math Marks")

plt.show()

plt.figure(figsize=(7,5))

plt.hist(df["Math"], bins=5)

plt.title("Distribution of Math Marks")
plt.xlabel("Math Marks")
plt.ylabel("Number of Students")

plt.show()

plt.figure(figsize=(7,5))

plt.scatter(df["Math"], df["Science"])

plt.title("Math vs Science")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

plt.show()
print(df.isnull().sum())
print(df.duplicated().sum())
df["Total"] = df["Math"] + df["Science"] + df["English"]

print(df)
df["Average"] = df["Total"] / 3

print(df)
topper = df.loc[df["Total"].idxmax()]

print(topper)
top3 = df.nlargest(3, "Total")
print(top3)
lowest = df.nsmallest(3, "Total")
print(lowest)   
print("Average Attendance of Students: ", df["Attendance"].mean())
print("Highest Attendance: ", df["Attendance"].max())
highest_attendance = df[df["Attendance"]>80]
print(highest_attendance)
print(df.groupby("Gender")["Total"].mean())
print(df.groupby("City")["Total"].mean())
plt.figure(figsize=(8,5))
plt.boxplot(df["Math"])
plt.title("Boxplot of Math Marks")
plt.ylabel("Math Marks")    
plt.show()
subjects = ["Math", "Science", "English"]
avg_marks = df["Math"].mean(), df["Science"].mean(), df["English"].mean()
plt.figure(figsize=(8,5))
plt.bar(subjects, avg_marks)
plt.title("Average Marks in Each Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()
# phase 3: Data Visualization of Student Data in Dashboard
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("student_data.csv")
df["Total"] = df["Math"] + df["Science"]
plt.figure(figsize=(12, 8))
#Graph 1 bar chat
plt.subplot(2, 2, 1)    
df["City"].value_counts().plot(kind="bar", color="skyblue")
plt.title("Number of Students in Each City")    
#Graph 2 pie chart
plt.subplot(2, 2, 2)
df["City"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=["lightgreen", "lightcoral", "lightskyblue"])
plt.title("Students Distribution by City")
plt.ylabel("")  # Hide y-label for pie chart
#Graph 3 line chart
plt.subplot(2, 2, 3)
plt.plot(df["Name"], df["Math"], marker="o", color="orange")
plt.title("Math Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Math Marks")
#Graph 4 top Student
plt.subplot(2, 2, 4)
top5 = df.nlargest(5, "Total")
plt.bar(top5["Name"], top5["Total"], color="purple")
plt.title("Top 5 Students by Total Marks")
plt.tight_layout()
plt.show()
# phase 4:data Analyst
df["Total"] = df["Math"] + df["Science"] + df["English"]
print(df[["Name","Total"]])
df["Percentage"] = df["Total"]/3
print(df[["Name","Percentage"]])
def grade(x):
    if x >= 90:
        return "A+"
    elif x >= 80:
        return "A"
    elif x >= 70:
        return "B"
    elif x >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Percentage"].apply(grade)

print(df[["Name", "Total", "Percentage", "Grade"]])
#phase 5: Professional Data Analysis
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Attendance"])
plt.title("Attendance of Students")
plt.xlabel("Student Name")
plt.ylabel("Attendance (in %)")
plt.xticks(rotation=45) 
plt.savefig("Attendance_Graph.png")
plt.show()
# Phase 6: Correlation Analysis
print(df[["Math", "Science", "English","Attendance"]].corr())
import seaborn as sns
plt.figure(figsize=(6,5))
sns.heatmap(df[["Math", "Science", "English","Attendance"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
df.to_csv("Student_Report.csv", index=False)
print("completed my project successfully")