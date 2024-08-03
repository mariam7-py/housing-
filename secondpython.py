# is there a relationship between NO2 concentration and proportion of non-retail acres per town ?

#state the hypothesis: H0= there is no relationship between NO2 concentration and proportion of non-retail acres per town
#H1= there is a relationship between NO2 concentration and proportion of non-retail acres per town

ax=sns.scatplot('NOX','INDUS', data=ratings_df)
scipy.stats.pearsonr(ratings_df[ratings_df['NOX'], ratings_df['INDUS'])

# since p-value< 0.05, we reject the Null Hypothesis and conclude that there is a relationship between NO2 concentration and proportion of non-retail acres per town.
