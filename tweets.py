import twint 

c = twint.Config()
c.Format = "{id}"
c.Search = "TAMU"
c.Filter_retweets = False
# c.Min_likes = 10
# c.Min_retweets = 10
c.Limit = 100000000
c.Lang = "en"
c.Store_csv = True
c.Output = "08-10.csv"
c.Since = "2020-08-10"
c.Until = "2020-08-11"
#c.Hide_output = True
twint.run.Search(c)