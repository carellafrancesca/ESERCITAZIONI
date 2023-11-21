package com.AbbonamentiPalestra.Repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.AbbonamentiPalestra.Class.Abbonati;

@Repository
public interface AbbonatiRepo extends CrudRepository<Abbonati, Long>{

	List<Abbonati> findByCittaDiNascita(String cittaDiNascita);	

}
