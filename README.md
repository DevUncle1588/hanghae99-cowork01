<h2 align="center">Team 6. Project_ J-GATI</h2>
<br>
<br>
<h3 align="left">1. Intro Project</h3>
<div>
<p>
J-GATI는 조깅 파트너를 모집하는 웹 애플리케이션입니다.
혼자하는 운동을 떠나 같이 동료를 모집하여 즐길 수 있으며, 
즐거운 조깅 모임을 만드실 수 있습니다.
현재 단계는 앱의 중심기능인 모집과 기본 서버를 토대로하는 기초 프레임을 만드는 단계이며,
앞으로 더 다양한 기능으로 여러분과 함께 할 예정입니다.
</p>
</div>
<br>
<br>
<hr/>
<h3 align="left">2. View Project</h3>
<br>
<br>
<hr/>
<h3 align="left">3. TECH</h3>
<br>
<br>
<hr/>
<h3 align="left">4. S.A(Starting Assignment)</h3>
  https://app.tryeraser.com/workspace/gather:6O2lSfydONva4UZbtable3?origin=share
<br>
<br>
<br>
<br>
<hr/>
<h3 align="left">5. Project Directory Structure</h3>
<br>
<br>
<hr/>
<h3 align="left">6. Function_PAGE</h3>
<br>
<br>
<hr/>
<h3 align="left">7. Function_API Table</h3>
<table width="100%">
  <thead>
    <tr>
      <th>기능</th>
      <th>Method</th>
      <th>URL</th>
      <th>request</th>
      <th>response </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> 회원가입 페이지 로드</td>
      <td>GET</td>
      <td></td>
      <td></td>
      <td>render_template('join.html', msg=msg)</td>
    </tr>
    <tr>
      <td> 메인화면 페이지 로드</td>
      <td>GET</td>
      <td></td>
      <td></td>
      <td> render_template('index.html', msg=msg)</td>
    </tr>
    <tr>
      <td>로그인</td>
      <td>POST</td>
      <td> /api/login</td>
      <td> {'id': id, 'pw'}</td>
      <td>
          로그인 성공 - {'result': 'success', 'token': token} 
          로그인 실패 - {'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'}
      </td>
    </tr>
    <tr>
      <td>회원가입</td>
      <td>POST</Td>
      <td> /api/membership</td>
      <td>{'id' : id, 'pw' : pw, 'email' : email}</td>
      <td> 가입 완료 메세지</td>
    </tr>
    <tr>
      <td>회원가입_중복검사</td>
      <td>POST</td>
      <td> /api/membership</td>
      <td>{'id' : id}</td>
      <td>
        중복 존재 - {'result': 'success', 'msg': '중복된 아이디입니다.'}
        중복 미존재 - {'result': 'fail', 'msg': '가능한 아이디입니다.'}
      </td>
    </tr>
    <tr>
      <td>리스트 페이지로드</td>
      <td>GET</td>
      <td></td>
      <td></td>
      <td> render_template('list.html', msg=msg)</td>
    </tr>
    <tr>
      <td>글 작성</td>
      <td>POST</td>
      <td> /api/write</td>
      <td>{ 'title' : title, 

 'date': date, 

 'place': place, 

 'attendance': attendance, 

 'content': content}</td>
      <td> 작성 글 데이터</td>
    </tr>
    <tr>
      <td>글 검색</td>
      <td>GET</td>
      <td> /api/search</td>
      <td> query={검색어}</td>
      <td> 검색 결과 리스트</td>
    </tr>
    <tr>
      <td>글 수정</td>
      <td>POST</td>
      <td> /api/update</td>
      <td>{ 'title' : title, 

'date': date, 

'place': place, 

'attendance': attendance, 

'content': content}</td>
      <td> 작성 글 데이터</td>
    </tr>
    <tr>
      <td>글 삭제</td>
      <td>POST</td>
      <td> /api/delete

</td>
      <td> {'ObjectID' : ObjectID}

</td>
      <td> 작성 글 데이터 삭제글 리스트

</td>
    </tr>
    <tr>
      <td>참가신청</td>
      <td>POST</td>
      <td> /api/applyParticipation

</td>
      <td> {'ObjectID' : ObjectID}

</td>
      <td> 작성 글 데이터

</td>
    </tr>
    <tr>
      <td>참</td>
      <td>POST</td>
      <td> /api/applyParticipation

</td>
      <td> {'ObjectID' : ObjectID}

</td>
      <td> 작성 글 데이터

</td>
    </tr>
  </tbody>
</table>
<br>
<br>
<hr/>
<h3 align="left">8. Members</h3>
<br>
<br>
<hr/>
<h3 align="left">9. Trouble Shooting</h3>


