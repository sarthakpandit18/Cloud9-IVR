import React from "react";
import UserPool from "../UserPool";
import { TextField, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { AccountContext } from "./Account";
const Signup = () => {

    const [email,setEmail] = React.useState("");
    const [password,setPassword] = React.useState("");

    const { getSession } = React.useContext(AccountContext);

    const navigate =  useNavigate();
    React.useEffect(() => {
        getSession().then(session => {
            navigate("/dashboard");
          })
    },[]);
    const onSubmit = (event) => {
        event.preventDefault();
        UserPool.signUp(email, password, [], null, (err, data) => {
            if (err){
                console.error(err);
            }
            console.log(data);
            navigate("/login");
        })

    };

    return (
        <div>
            <form onSubmit={onSubmit}>
            <TextField id="email" label="Email" variant="standard" onChange={(event) => setEmail(event.target.value)} value={email}  />
                <br/>
                <TextField id="password" label="Password" variant="standard" value={password} 
                onChange={(event) => setPassword(event.target.value)}  /> <br/>
                 <br/>
                <Button variant="contained" type="submit" >Sign Up</Button>
            </form>
        </div>
    );
};

export default Signup;