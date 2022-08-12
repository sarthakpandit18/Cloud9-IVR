import React, { useState, useContext } from "react";
import { AccountContext } from "./Account";
import { TextField, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
const Login = () => {

    const [email,setEmail] = React.useState("");
    const [password,setPassword] = React.useState("");
    
    const { authenticate, getSession } = useContext(AccountContext);
    const navigate =  useNavigate();
    React.useEffect(() => {
        getSession().then(session => {
             navigate("/dashboard");
          })
    },[]);

    const onSubmit = (event) => {
        event.preventDefault();
        authenticate(email,password).then( data => {
            navigate("/dashboard");
            console.log("yaay.. logged in", data)
        })
        .catch(err => {
            console.log("Nayy..", err);
            alert('Invalid credentials')
         
        })


    };


    return (
        <div>
            <form onSubmit={onSubmit}>
                <TextField id="email" label="Email" variant="standard" onChange={(event) => setEmail(event.target.value)} value={email}  />
                <br/>
                <TextField id="password" type="password" label="Password" variant="standard" value={password} 
                onChange={(event) => setPassword(event.target.value)}  />
                <br/>
                <br/>
                <Button variant="contained" type="submit">Login</Button>
            </form>
            
        </div>
    );
};

export default Login;