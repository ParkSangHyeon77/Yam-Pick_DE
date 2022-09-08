from flask import Blueprint, render_template, session
import pandas as pd
import json
import plotly
import plotly.express as px
from yp.models import tb_user

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def main():
   if 'user' in session:
      user_email = session.get("user")
      user = tb_user.query.filter_by(user_email=user_email).first()
      return render_template("main.html", username = user.user_name, login = True)
   else:
      return render_template("main.html", login = False)


@bp.route('/data')
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City', 
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('notdash.html', graphJSON=graphJSON)

