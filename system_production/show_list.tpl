<h3>System Users</h3>
<table border="1">
%for row in rows:
    <tr>
    %for user in row[1:]:
        <td>{{user}}</td>
    %end
    </tr>
%end
</table>

 <p>
    <a href="/new_user">New User</a>
</p>


