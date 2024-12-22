import React, { useState } from "react";
import "./signin.css";
import logo from "../assets/Logo.png";
import form from "../assets/form.png";

const Signin = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const validateForm = () => {
    const newErrors = {};

    if (!formData.email.trim()) {
      newErrors.email = "Email is required.";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Email is invalid.";
    }

    if (!formData.password.trim()) {
      newErrors.password = "Password is required.";
    } else if (formData.password.length < 6) {
      newErrors.password = "Password must be at least 6 characters.";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(false);
    if (validateForm()) {
      setSubmitted(true);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  return (
    <div>
      <div className="title">
        <img src={logo} alt="Logo" />
        <h2>DashRHi</h2>
      </div>
      <div className="signin-container">
        <div className="signin-card">
          <h2 className="welcome">Welcome</h2>
          <h3>Sign In</h3>
          {submitted && (
            <p className="success-message">Signed in successfully!</p>
          )}
          <form className="signin-form" onSubmit={handleSubmit}>
            <div>
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="Enter your email"
              />
              {errors.email && <p className="error-message">{errors.email}</p>}
            </div>
            <div>
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                placeholder="Enter your password"
              />
              {errors.password && (
                <p className="error-message">{errors.password}</p>
              )}
            </div>
            <div className="checkbox-container">
              <div>
                <input type="checkbox" id="remember" />
                <label className="remember">Remember me</label>
              </div>
              <p>forgot password?</p>
            </div>
            <button type="submit" className="login-button">
              Login
            </button>
          </form>
        </div>
        <img src={form} alt="Side Logo" className="side-image" />
      </div>
    </div>
  );
};

export default Signin;
