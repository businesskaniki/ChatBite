import CenterBar from './centerbar/CenterBar';
import LeftBar from './leftbar/LeftBar';
import Navbar from './navigation/Navbar';
import RightBar from './rightbar/RightBar';

const Home = () =>
  (
    <section className="h-screen bg-white">
      <Navbar />
      <div className="bg-white h-5/6 flex px-12 my-8 g-16">
        <div className="w-1/3 bg-black rounded-lg">
          <LeftBar />
        </div>
        <div className="w-1/3">
          <CenterBar />
        </div>
        <div className="w-1/3 h-1/2 bg-black rounded-lg">
          <RightBar />
        </div>
      </div>
    </section>
  );
export default Home;
