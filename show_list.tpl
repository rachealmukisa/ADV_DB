<p>Todo List</p>
<table border="1">
%for row in rows:
    <tr>
    %for item in row[1:]:
        <td>{{item}}</td>
    %end
    </tr>
%end
</table>

 <p>
    <a href="/new_item">New item</a>
</p>


