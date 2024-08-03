# What is the impact of an additional weighted distance to the five Boston employment centres on the median value of owner occupied homes? (Regression analysis)
#A= 0.05

X=ratings_df['DIS']
Y=ratings_df['MDEV']
X=sm.add_constant(X)

model=sm.OLS(Y,X).fit()
predictions=predict(X)

# print out the statistics result
print (model summary)

# at p value more than 0.05, we fail to reject the Null hypthesis, and there is no impact to additional an additional weighted distance to the five Boston employment centres on the median value of owner occupied homes
# at p value less than 0.05, we reject the null hypothesis and there is an impact to an additional weighted distance to the five boston employment centres on the median value of owner occupied Homes 

# present the MDEV by boxplot 
ax=sns.boxplot(x='DIS', y='MDEV', data=ratings_df)
plt.show()
