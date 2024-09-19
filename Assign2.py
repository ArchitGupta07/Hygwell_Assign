import pandas as pd
from scipy.stats import pearsonr, chi2_contingency

data = pd.read_csv('traffic.csv', header=None, names=['event', 'date', 'country', 'city', 'artist', 'album', 'track', 'linkid', 'uuid'])

pageview_data = data[data['event'] == 'pageview']
click_data = data[data['event'] == 'click']
preview_data = data[data['event'] == 'preview']



# =======================================================================================
# =======================================================================================
# Total and Daily page view events
total_pageviews = pageview_data.shape[0]
pageview_data['date'] = pd.to_datetime(pageview_data['date'])
daily_pageviews = pageview_data.groupby('date').size()
average_pageviews_per_day = daily_pageviews.mean()


# =======================================================================================
# =======================================================================================
# Analysis of other events 
event_counts = data['event'].value_counts()


# =======================================================================================
# =======================================================================================
#Geographical Distribution
country_distribution = pageview_data['country'].value_counts()

# =======================================================================================
# =======================================================================================
# Click through rate analysis
total_clicks = click_data.shape[0]
overall_ctr = total_clicks / total_pageviews

link_clicks = click_data.groupby('linkid').size()
link_pageviews = pageview_data.groupby('linkid').size()
link_previews = preview_data.groupby('linkid').size()
link_data = pd.DataFrame({'clicks': link_clicks, 'pageviews': link_pageviews,"previews":link_previews}).fillna(0)
link_data['ctr'] = link_data['clicks'] / link_data['pageviews']



# =======================================================================================
# =======================================================================================
#linear test Pearson correlation coefficient
corr, p_value = pearsonr(link_data['clicks'], link_data['previews'])

#Binary Test chi-square test
contingency_table = pd.crosstab(link_data['previews'] > 0, link_data['clicks'] > 0)
chi2, p_chi, dof, ex = chi2_contingency(contingency_table)




print(f"Total Pageviews: {total_pageviews}")
print(f"Average Pageviews Per Day: {average_pageviews_per_day}")
print(f"Event Counts:\n{event_counts}")
print(f"Country Distribution:\n{country_distribution}")
print(f"Overall CTR: {overall_ctr}")
print(f"CTR by Link:\n{link_data[['ctr']]}")
print(f"Pearson Correlation between Clicks and Pageviews: {corr}, p-value: {p_value}")
print(f"Chi-Square test: Chi2 = {chi2}, p-value = {p_chi}")
