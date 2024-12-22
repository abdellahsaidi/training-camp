import React, { useState } from "react";
import "./FormContainer.css";

const FormContainer = () => {
  // State for form data
  const [formData, setFormData] = useState({
    fullName: "",
    startDate: "",
    dateEnd: "",
    reason: "",
  });

  // State for submission feedback
  const [submitted, setSubmitted] = useState(false);

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted:", formData);

    // Show success message
    setSubmitted(true);

    // Reset form after submission
    setFormData({
      fullName: "",
      startDate: "",
      dateEnd: "",
      reason: "",
    });

    // Clear success message after 3 seconds
    setTimeout(() => setSubmitted(false), 3000);
  };

  return (
    <form className="form-container1" onSubmit={handleSubmit}>
      <h2 className="h2-form1">Leave Request</h2>
      <div className="form-section1">
        <div className="first-sec1">
          <div>
            <label htmlFor="fullName">Full Name :</label>
            <input
              type="text"
              id="fullName"
              name="fullName"
              placeholder="Typing"
              value={formData.fullName}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="startDate">Start Date :</label>
            <input
              type="date"
              id="startDate"
              name="startDate"
              value={formData.startDate}
              onChange={handleChange}
              required
            />
          </div>
          <div>
            <label htmlFor="dateEnd">Date End :</label>
            <input
              type="date"
              id="dateEnd"
              name="dateEnd"
              value={formData.dateEnd}
              onChange={handleChange}
              required
            />
          </div>
        </div>
        <div className="scd-sec1">
          <div>
            <label htmlFor="reason">Reason for Leave :</label>
            <textarea
              id="reason"
              name="reason"
              placeholder="Type your reason here..."
              value={formData.reason}
              onChange={handleChange}
              required
            ></textarea>
          </div>
        </div>
      </div>
      <button type="submit" className="create-account-button">
        Submit Request
      </button>
      {submitted && (
        <p className="success-message">
          Your leave request has been submitted successfully!
        </p>
      )}
    </form>
  );
};

export default FormContainer;
