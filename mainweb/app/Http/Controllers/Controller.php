<?php

namespace App\Http\Controllers;

use Illuminate\Support\Facades\DB;
use Illuminate\Http\Request;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function main_page(){
        return view("main");
    }

    public function result_page(){
        return view("result");
    }
    
    public function resultname(Request $req){
        $name = $req["name"];
        $query = "select  * from result_all_detail where student_name LIKE '%".$name."'GROUP BY roll limit 20";
    
        $result = DB::select($query);
        //dd($result);
        return view('resultviewname',["result"=>$result]);

        
    }
    public function resultop(Request $req){
        $roll = $req["roll"];
        $query = "select DISTINCT * from result_all_detail where roll LIKE '%".$roll."%'  GROUP by roll limit 10";
        $result = DB::select($query);
        //dd($result);
        return view('resultview',["result"=>$result]);

        
    }

    public function mainresult(Request $req,$roll){
        //$roll = $req["roll"];
        $query = "select * from result_all_detail where roll ='".$roll."'";
        $result = DB::select($query);
        //dd($result);
        return view("mainresult",["result" => $result]);

    
    }
}
