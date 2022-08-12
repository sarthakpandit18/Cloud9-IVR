import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import CloudIcon from '@mui/icons-material/Cloud';
import { AccountContext } from './Account';
import { Link as navLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";

const pages = [
  {
    name: "Login",
    link: "/login",
  },
  {
    name: "Signup",
    link: "/signup",
  }
  
];
const settings = [ 
  {
    name: "Dashboard",
    link: "/dashboard",
  },
  {
    name: "Logout",
    link: "/login", // do not change this
  }];

const ResponsiveAppBar = () => {
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = (event) => {
    setAnchorElNav(null);
  };

  
  const navigate =  useNavigate();
  const handleCloseUserMenu = (event) => {
    if (event === 'Logout'){
      setStatus(false);
      logout();
    }
    setAnchorElUser(null);
  };
  
  const [status, setStatus] = React.useState(false);
  const { getSession, logout } = React.useContext(AccountContext)
  React.useEffect(() => {
    console.log("inside use effect")
      getSession().then(session => {
        console.log("inside get session",status)
          setStatus(true)
      })
  },[getSession(),status])

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <CloudIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            CLOUD-9
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
           
              {status ? null : <div>
              {pages.map((page) => (
                  <MenuItem
                    key={page.name}
                    onClick={handleCloseNavMenu}
                    component={navLink}
                    to={page.link}
                  >
                  <Typography textAlign="center">{page.name}</Typography>
                </MenuItem>
              ))}
              </div>}
              
              
            </Menu>
          </Box>
          <CloudIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href=""
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            CLOUD-9
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
          {status ? null : <div style={{flexDirection:"row"}}>
            {pages.map((page) => (
              <Button
                key={page.name}
                onClick={() => navigate(page.link)}
                sx={{ my: 2, color: 'white',
                //  display: 'block' 
                }}
              >
                {page.name}
              </Button>
            ))}
            </div>
          }
          </Box>

          <Box sx={{ flexGrow: 0 }}>
          {status ?  <div><Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
              </IconButton>
            </Tooltip>
            </div>: null}
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={(event) => handleCloseUserMenu(event)}
            >
              {status ?  <div>
              {settings.map((page) => (
                  <MenuItem
                    key={page.name}
                    onClick={(event) => handleCloseUserMenu(page.name)}
                    component={navLink}
                    to={page.link}
                  >
                  <Typography textAlign="center">{page.name}</Typography>
                </MenuItem>
              ))}
              </div>:null}
              {/* {settings.map((setting) => (
                <MenuItem key={setting} onClick={handleCloseUserMenu}>
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))} */}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
export default ResponsiveAppBar;

// reference: https://mui.com/ --> app bar with responsive menu