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

# Define route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/table')
def table():
  
    # # Group rows into teams
    # 
    df = pd.read_csv('Aptithon.csv')
    df1 = df.drop(['Unnamed: 2', 'Unnamed: 3'], axis=1)
    df2 = df1.iloc[:, :5]
    columns = df2.columns.tolist()  # Get column names
    print(columns)
    print(df2.head())
    teams = group_teams(df2)
    return render_template('table.html', teams=teams, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
