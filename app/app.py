import pprint
import json
import os
import sys
import traceback


app = Flask(__name__)
with open("./config.{0}.json".format(os.environ['APP_ENV'])) as data_file:    
@app.route('/')
def index():
  ventures = os.environ['VENTURES'].split(',')
  # print(json.dumps(ventures), file=sys.stderr)
  return render_template('index.html', ventures = ventures)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8888, debug=True, processes=10)
