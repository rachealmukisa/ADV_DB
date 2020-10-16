<p>Todo List - Experimental Version</p>
<table border="1">
%for row in rows:
    <tr>
        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
        <td>{{row[2]}}</td>
        <td>{{row[3]}}</td>
        <td><a href="/update_user/{{row[0]}}">EDIT</a></td>
        <td><a href="/delete_user/{{row[0]}}">DELETE</a></td>
    </tr>
%end
</table>
<a href="/new_user">New User</a>
<hr/>


<!---
<h3>System Users</h3>
<table border="1">
%for row in rows:
    <tr>
    %for user in row[1:]:
        <td>{{user}}</td>
    %end
    <td>
            <a href="/delete_user/{{row[0]}}">DELETE</a>    
    </td>
    </tr>
%end
</table>

 <p>
    <a href="/new_user">New User</a>
</p> ----> 