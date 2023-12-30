// index.js
const express = require('express');
const session = require('express-session');
const passport = require('passport');
const auth = require('./auth');

const app = express();
const port = 3000;

// کانفیگ Passport.js
auth();

app.use(express.urlencoded({ extended: true }));
app.use(session({ secret: 'your-secret-key', resave: false, saveUninitialized: false }));
app.use(passport.initialize());
app.use(passport.session());

// مسیر لاگین
app.post('/login',
  passport.authenticate('local', {
    successRedirect: '/',
    failureRedirect: '/login',
    failureFlash: true
  })
);

// مسیر خروج
app.get('/logout', (req, res) => {
  req.logout();
  res.redirect('/');
});

// مسیر صفحه اصلی
app.get('/', (req, res) => {
  if (req.isAuthenticated()) {
    res.send(`Hello, ${req.user.username}! <a href="/logout">Logout</a>`);
  } else {
    res.send('Hello, guest! <a href="/login">Login</a>');
  }
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

