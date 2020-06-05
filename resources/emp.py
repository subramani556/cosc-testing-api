from flask_restful import Resource,reqparse
from db import query

class Emp(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('empno',type=int,required=True,help="empno cannot be left blanK!")
        data=parser.parse_args()
        try:

            return  query("""select * from testapi.emp where empno={data['empno']};""")

        except:
            return  {"message": "there is error connecting database."},500

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('empno',type=int,required=True,help='empno cannot be left blank!')
        parser.add_argument('ename',type=str,required=True,help='ename cannot be left blank!')
        parser.add_argument('job',type=str,required=True,help='job cannot be left blank!')
        parser.add_argument('mgr',type=int,required=True,help='mge cannot be left blank!')
        parser.add_argument('hiredate',str=int,required=True,help='empno cannot be left blank!')
        parser.add_argument('sal',type=str,required=True,help='empno cannot be left blank!')
        parser.add_argument('comm',type=int)
        parser.add_argument('deptno',type=str,required=True,help='empno cannot be left blank!')
        data=parser.parse_args()

        try:
            return  query(f"""insert into testapi.emp values({data['empno']},
                                                            '{data['ename']}',
                                                            '{data['job']}',
                                                            '{data['mgr']}',
                                                            '{data['hiredate']}',
                                                            '{data['sal']}'',
                                                            '{data['comm']}',
                                                            {data['deptno']})""")

        except:
            return  {"message": "there is error connecting database."},500

        return {"MESSAGE":"succesfully inserted"}