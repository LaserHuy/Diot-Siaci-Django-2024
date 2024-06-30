import "./Footer.css";

import { AiFillFacebook } from "react-icons/ai";
import { FaMapMarkerAlt } from "react-icons/fa";
import { MdMarkEmailRead } from "react-icons/md";
import { BsTwitter, BsInstagram, BsYoutube, BsFillTelephoneForwardFill } from "react-icons/bs";

const Footer = () => {
  return (
    <div className="footer">
      <footer>
        <div className="container">
            <div className="sec about">
                <h2> About Me</h2>
                <p>I'm student from Wild Code School. I want to apply to Internship at Diot-Siaci</p>
                <ul className="sci">
                    <li><a href="/"><AiFillFacebook /></a></li>
                    <li><a href="/"><BsTwitter /></a></li>
                    <li><a href="/"><BsInstagram /></a></li>
                    <li><a href="/"><BsYoutube /></a></li>
                </ul>
            </div>
            <div className="sec quickLinks">
              <h2>Quick Links</h2>
              <ul>
                <li><a href="#">About</a></li>
                <li><a href="#">FAQ</a></li>
                <li><a href="#">Privacy Policy</a></li>
                <li><a href="#">Help</a></li>
                <li><a href="#">Terms & Conditions</a></li>
                <li><a href="#">Contacts</a></li>
              </ul>
            </div>
            <div className="sec contact">
              <h2>Contact Info</h2>
              <ul className="info">
                <li>
                  <span><FaMapMarkerAlt /></span>
                  <span>44 Rue Alphonse Penaud<br/>75020 Paris</span>
                </li>
                <li>
                  <span><BsFillTelephoneForwardFill /></span>
                  <p><a href="tel:0658364784">01 23 45 67 89</a></p>
                </li>
                <li>
                  <span><MdMarkEmailRead /></span>
                  <p><a href="mailto:laser2u02@gmail.com">laser2u02@gmail.com</a></p>
                </li>
              </ul>
            </div> 
        </div>
      </footer>
    </div>
  )
}

export default Footer;