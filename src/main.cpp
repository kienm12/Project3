#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <matplot/matplot.h>
#include <pybind11/stl.h>


using namespace std;
using namespace matplot;

namespace py = pybind11;

int plot_wave(py::array_t<int, py::array::c_style | py::array::forcecast>  &input_vector, string tytul, string nazwa , double rate){
    std::vector<int> array_vector(input_vector.size());
    std::memcpy(array_vector.data(), input_vector.data() , input_vector.size()*sizeof(int));

    title(tytul);
    xlabel("Czas");        
    xticks({0, 0.1*rate, 0.2*rate, 0.3*rate,0.4*rate, 0.5*rate,0.6*rate});
    xticklabels({"00:00s","00:10s", "00:20s", "00:30s", "00:40s", "00:50s", "01:00s"});

    plot(array_vector);        // does not draw

    show();

    return 0;
}

int plot_wave_to_file(py::array_t<int, py::array::c_style | py::array::forcecast>  &input_vector, string tytul, string nazwa_pliku, double rate){
    std::vector<int> array_vector(input_vector.size());
    std::memcpy(array_vector.data(), input_vector.data() , input_vector.size()*sizeof(int));
    figure(true);
    title(tytul);
    xlabel("Czas");        
    xticks({0, 0.1*rate, 0.2*rate, 0.3*rate,0.4*rate, 0.5*rate,0.6*rate});
    xticklabels({"00:00s","00:10s", "00:20s", "00:30s", "00:40s", "00:50s", "01:00s"});
    plot(array_vector);
    save(nazwa_pliku);
    return 0;
}

int plot_inne(py::array_t<int, py::array::c_style | py::array::forcecast>  &input_vector, string tytul, string nazwa_pliku ){
    std::vector<int> array_vector(input_vector.size());
    std::memcpy(array_vector.data(), input_vector.data() , input_vector.size()*sizeof(int));
    figure(true);
    title(tytul);
    plot(array_vector);
    save(nazwa_pliku);
    return 0;
}

int plot_wave2(py::array_t<int, py::array::c_style | py::array::forcecast>  &input_vector, string tytul, string nazwa_pliku , double rate){
    std::vector<int> array_vector(input_vector.size());
    std::memcpy(array_vector.data(), input_vector.data() , input_vector.size()*sizeof(int));
    figure(true);
    title(tytul);
    plot(array_vector);
    save(nazwa_pliku);
    return 0;
}

int plot_wave3(py::array_t<int, py::array::c_style | py::array::forcecast>  &input_vector, py::array_t<int, py::array::c_style | py::array::forcecast>  &input_vector2, string tytul, string nazwa_pliku ){
    std::vector<int> array_vector(input_vector.size());
    std::memcpy(array_vector.data(), input_vector.data() , input_vector.size()*sizeof(int));

    std::vector<int> array_vector2(input_vector2.size());
    std::memcpy(array_vector2.data(), input_vector2.data() , input_vector2.size()*sizeof(int));

    figure(true);
    title(tytul);
    plot(array_vector, array_vector2);        // does not draw
    save(nazwa_pliku);
    return 0;
}



PYBIND11_MODULE(_core, m) {
    m.def("plot_wave_to_file", &plot_wave_to_file);
    m.def("plot_inne", &plot_inne);
    m.def("plot_wave", &plot_wave);
    m.def("plot_wave2", &plot_wave2);
    m.def("plot_wave3", &plot_wave3);
}

