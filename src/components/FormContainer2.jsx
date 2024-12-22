import React, { useState } from "react";
import "./FormContainer.css";

const FormContainer = () => {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    position: "",
    role: "",
    photo: null,
  });
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };
  const handleFileChange = (e) => {
    setFormData((prevData) => ({
      ...prevData,
      photo: e.target.files[0],
    }));
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);
    alert("Account Created Successfully!");
  };

  return (
    <form className="form-container" onSubmit={handleSubmit}>
      <h2 className="h2">Create Account</h2>
      <div className="form-section">
        <div className="first-sec">
          <div>
            <label htmlFor="firstName">First Name</label>
            <input
              type="text"
              id="firstName"
              name="firstName"
              placeholder="Typing"
              value={formData.firstName}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="lastName">Last Name</label>
            <input
              type="text"
              id="lastName"
              name="lastName"
              placeholder="Typing"
              value={formData.lastName}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              name="email"
              placeholder="Typing"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
        </div>
        <div className="scd-sec">
          <div>
            <label htmlFor="position">Position</label>
            <input
              type="text"
              id="position"
              name="position"
              placeholder="Typing"
              value={formData.position}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="role">Role</label>
            <input
              type="text"
              id="role"
              name="role"
              placeholder="Typing"
              value={formData.role}
              onChange={handleChange}
              required
            />
          </div>
          <div className="photo-upload">
            <label htmlFor="photo">Add Photo</label>
            <input
              type="file"
              id="photo"
              name="photo"
              accept="image/*"
              onChange={handleFileChange}
            />
          </div>
        </div>
      </div>
      <button type="submit" className="create-account-button">
        Create Account
      </button>
    </form>
  );
};

export default FormContainer;
