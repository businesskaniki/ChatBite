import React from "react";
import { Link } from "react-router-dom";
import { FaHome, FaEnvelope, FaBell, FaEdit } from "react-icons/fa";

function Navbar() {
  return (
    <nav className="flex items-center justify-between bg-blue-700 py-2 px-4 fixed bottom-0 left-0 right-0 lg:relative lg:bg-blue-700 lg:py-2 lg:px-8 shadow-md">
      <div className="hidden lg:flex items-center justify-between">
        <div className="flex-shrink-0 flex items-center justify-between">
          <img
            className="block lg:hidden h-8 w-auto"
            src="https://designpress.com/wp-content/uploads/2013/02/popular-logos/sony-ericsson-logo.jpg"
            alt="Company Logo"
          />
          <img
            className="hidden lg:block h-8 w-auto"
            src="https://designpress.com/wp-content/uploads/2013/02/popular-logos/sony-ericsson-logo.jpg"
            alt="Company Logo"
          />
        </div>
        <div className="flex">
          <div className="flex items-center p-4">
            <a href="/" className="text-lg font-medium text-white">
              Home
            </a>
            <FaHome className="ml-2 text-white" />
          </div>
          <div className="flex items-center px-4">
            <a href="/" className="text-lg font-medium text-white">
              posts
            </a>
            <FaEdit className="ml-2 text-white" />
          </div>
          <div className="flex items-center px-4">
            <a href="/" className="text-lg font-medium text-white">
              notification
            </a>
            <FaBell className="ml-2 text-white" />
          </div>
          <div className="flex items-center px-4">
            <a href="/" className="text-lg font-medium text-white">
              messages
            </a>
            <FaEnvelope className="ml-2 text-white" />
          </div>
        </div>
      </div>
      <div class="hidden lg:flex items-center">
        <ul className="flex items-center">
          <li>
            <Link
              to="/login"
              className="block mx-4 text-white hover:text-gray-700"
            >
              Login
            </Link>
          </li>
          <li>
            <Link
              to="/signup"
              className="block mx-4 text-white hover:text-gray-200"
            >
              Sign up
            </Link>
          </li>
        </ul>
        <h5 className="p-6 text-white">profile</h5>
        <div class="border-2 border-gray-300">
          <img
            class="w-10 h-10"
            src="https://via.placeholder.com/150"
            alt="Profile Picture"
          />
        </div>
      </div>
      <div className="flex items-center justify-between w-full lg:hidden">
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
            <FaHome className="ml-2 text-white" />
          </a>
        </div>
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
            <FaEdit className="ml-2 text-white" />
          </a>
        </div>
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
            <FaEnvelope className="ml-2 text-white" />
          </a>
        </div>
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
            <FaBell className="ml-2 text-white" />
          </a>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
