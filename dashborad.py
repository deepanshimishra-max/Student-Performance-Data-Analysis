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
