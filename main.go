package main

import (
    "fmt"
    "net/http"
)

func readIpAndMask() {

}

func hello(w http.ResponseWriter, req *http.Request) {

    fmt.Fprintf(w, "nello\n")
}

func remoteAddress(w http.ResponseWriter, req *http.Request) {

    fmt.Fprintf(w, "Ip: %v", req.RemoteAddr)
}

func headers(w http.ResponseWriter, req *http.Request) {

    for name, headers := range req.Header {
        for _, h := range headers {
            fmt.Fprintf(w, "%v: %v\n", name, h)
        }
    }
}

func main() {

    http.HandleFunc("/hello", hello)
    http.HandleFunc("/headers", headers)
    http.HandleFunc("/remoteAddress", remoteAddress)

    http.ListenAndServe(":8090", nil)
}