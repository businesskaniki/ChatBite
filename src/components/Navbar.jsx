import React from 'react';
import { FaHome, FaEnvelope, FaBell, FaEdit} from 'react-icons/fa';

function Navbar() {
  return (
    <nav className="flex items-center justify-between bg-blue-300 py-2 px-4 fixed bottom-0 left-0 right-0 lg:relative lg:bg-blue-300 lg:py-4 lg:px-8">
      <div className="hidden lg:flex items-center">
        <div className="flex items-center p-4">
          <a href="/" className="text-lg font-medium text-red-800">
          Home
        </a>
        <FaHome className="ml-2 text-gray-500" />
        </div>
        <div className="flex items-center px-4">
          <a href="/" className="text-lg font-medium text-red-800">
          posts
        </a>
        <FaEdit className="ml-2 text-gray-500" />
        </div>
        <div className="flex items-center px-4">
          <a href="/" className="text-lg font-medium text-red-800">
          notification
        </a>
        <FaBell className="ml-2 text-gray-500" />
        </div>
        <div className="flex items-center px-4">
          <a href="/" className="text-lg font-medium text-red-800">
          messages
        </a>
        <FaEnvelope className="ml-2 text-gray-500" />
        </div>
      </div>
      <div class="hidden lg:flex items-center">
      <h5 className="p-6">profile</h5>
      <div class="border-2 border-gray-300">
        <img class="w-10 h-10" src="https://via.placeholder.com/150" alt="Profile Picture" />
      </div>
    </div>
      <div className="flex items-center justify-between w-full lg:hidden">
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
          <FaHome className="ml-2 text-gray-500" />
        </a>
        </div>
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
          <FaEdit className="ml-2 text-gray-500" />
        </a>
        </div>
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
          <FaEnvelope className="ml-2 text-gray-500" />
        </a>
        </div>
        <div className="flex items-center">
          <a href="/" className="text-lg font-medium text-red-800">
          <FaBell className="ml-2 text-gray-500" />
        </a>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
