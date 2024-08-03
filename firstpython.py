
# provide a median value for owner occupied Houses 
ratings_df['MDEV'].Median()
ax=sns.boxplot(y='MDEV', data=ratings_df) 
plt.show()

# calculate using anova , test for equality of variances 
scipy.stats.levene (ratings_df[ratings_df['AGE'] == '35 years and younger'],['eval'],
                    ratings_df[ratings_df['AGE'] == 'between 35 years old 70 years old'],['eval'],
                    ratings_df[ratings_df['AGE'] == '70 years old and older'],['eval']
                    center='mean')   
                    
thirty_five_lower_eval=ratings_df[ratings_df['AGE'] == '35 years and older'],['eval']
thirty_fiveseventy_eval=ratings_df[ratings_df['AGE'] == 'between 35 years old and seventy'], ['eval']
seventy_yearsolder_eval=ratings_df[ratings_df['AGE'] == ' 70 years and older'], ['eval']

f_statistic, P_value= spicy.stats.f_oneway( thirty_five_lower_eval, thirty_fiveseventy_eval, seventy_yearsolder_eval)
print("F_statistic: {0}, p_value: {1}".format(f_statistic, p_value))
                    
                                                                                        

