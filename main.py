from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
app.static_folder = 'assets'

def group_teams(df):
    teams = []
    team = []
    for index, row in df.iterrows():
        if not pd.isnull(row['Team No']):
            if team:
                teams.append(team)
                team = []
        team.append(row.values.tolist())
    if team:
        teams.append(team)
    return teams    

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
    # Read the Excel file
    df = pd.read_csv('ap.csv')
    df1 = df.drop(['Name of Participant', 'Unnamed: 3'], axis=1)
    df2 = df1.iloc[:, :5]
    columns = df2.columns.tolist()  # Get column names

    # Group rows into teams
    teams = group_teams(df2)

    return render_template('table.html', teams=teams, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
