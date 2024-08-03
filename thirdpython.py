# What is the impact of an additional weighted distance to the five Boston employment centres on the median value of owner occupied homes? (Regression analysis)
#A= 0.05

X=ratings_df['DIS']
Y=ratings_df['MDEV']
X=sm.add_constant(X)

model=sm.OLS(Y,X)
predictions=predict(X)
