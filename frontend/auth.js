// auth.js
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const serverName = process.env.SERVER_NAME || 'Default Server';
passport.use(new LocalStrategy(
  (username, password, done) => {
    // در این قسمت باید احراز هویت کاربران را انجام دهید
    // مثال: اطلاعات کاربر از یک دیتابیس بررسی شود
    if (username === 'user' && password === 'password') {
      return done(null, { id: 1, username: 'user' });
    } else {
      return done(null, false, { message: 'Invalid credentials' });
    }
  }
));

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  // در این قسمت اطلاعات کاربر با استفاده از id به دست می‌آید
  // مثال: اطلاعات از دیتابیس بخوانید
  const user = { id: 1, username: 'user' };
  done(null, user);
});

console.log(`Server Name: ${serverName}`);
