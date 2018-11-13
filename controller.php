
<?php
require_once 'connection.php';
class EPIC_Controller
{

       public function register($post)
    {
        $response = [];
        $valuelist = [];
        $valuelist["Email"] = $post['Email'];
        $valuelist["Password"] = $post['Password'];
        $valuelist["Status"] = "active";
        $Res = insert_DATA("User_Accounts", $valuelist);
        if ($Res != false) {
            $response['status'] = 'Success';
        } else {
            $response['status'] = 'Error';
        }
        return $response;
    }

    public function login($post)
    {
        $response = [];
        $email = $post['Email'];
        $password = $post['Password'];
        $Query = "SELECT * FROM User_Accounts WHERE Email='$email' AND Password='$password'";
        $Res = fetchdata($Query);
        if ($Res['UID']) {
            if ($Res['Status'] == "active") {
                $response['status'] = 'Success';
                $response['email'] = $email;
                $response['id'] = md5(uniqid());
                $response['uid'] = $Res['UID'];
                $_SESSION['id'] = $response['id'];
            }
            else if ($Res['status'] == "disabled") {
                $response['status'] = 'disabled';
            }
        } else {
            $response['status'] = 'Error';
        }
        return $response;
    }

}