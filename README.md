  
# housing near Charles river (t-test)
# we calculate the median values
ratings_df[ratings_df['CHAS']=='1'],['eval'].median()
ratings_df[ratings_df['CHAS']=='0'],['eval'].median()

# we use a barplot function
pyplot.bar([ratings_df['CHAS'],(sort='false'),color=['pink','blue']
pyplot.xlabel=('CHAS')
pyplot.ylabel=('price')
pyplot.title('Median of house prices near Charles river')

# we test the hypothesus Ho= null ' there is no difference in the median values between houses near Charles river and far ones'
# H1= median1 is not equal to median 2 ' there is a difference in the median values btween the prices of houses near Charles river and far ones'

scipy.stats.levene(ratings_df[ratings_df['CHAS'] == '1'],['eval'],
                   ratings_df[ratings_df['CHAS'] == '0'],['eval'], center = 'median')
# since p value is greater than 0.05, we can assume equality of variances

scipy.stats.ttest_ind(ratings_df[ratings_df['CHAS'] == '1'],['eval'],
                      ratings_df[ratings_df['CHAS'] == '0'],['eval'], equal_var= true)
# since p value is less than 0.0, we reject the null hypothesis as there is enough proof that there is a statistical difference in House prices based on proximity to Charles river.                    
                   
