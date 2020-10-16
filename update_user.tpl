<p>Update Task</p>
<form action="/update_user" method="POST">
    <input type="hidden" size="100" maxlength="100" name="id" value="{{str(row[0])}}" /><br /><br />
    <input type="text" size="100"  name="f_name" value="{{str(row[1])}}" /><br /><br />
    <input type="text" size="100"  name="myemail" value="{{str(row[2])}}" /><br /><br />
    <input type="text" size="100"  name="msg" maxlength="100" value="{{str(row[3])}}" /><br /><br />
    <input type="submit" name="update" value="Update">
</form>