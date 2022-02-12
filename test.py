import pandas as pd
from psaw import PushshiftAPI

if __name__ == '__main__':
    pd.set_option('max_colwidth', 500)
    pd.set_option('max_columns', 50)

    # Initialize PushShift
    api = PushshiftAPI()

    api_request_generator = api.search_submissions(q='(Corona)|(Pandemic)', score = ">2000")
    aita_submissions = pd.DataFrame([submission.d_ for submission in api_request_generator])
    aita_submissions.shape
    hihi = aita_submissions[['title', 'score']].sample(10)
    i = 3